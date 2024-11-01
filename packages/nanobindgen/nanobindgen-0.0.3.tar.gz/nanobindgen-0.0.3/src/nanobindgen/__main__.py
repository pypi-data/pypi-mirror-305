import argparse
from pathlib import Path
from typing import Dict, List, Optional

import tree_sitter_cpp
import tree_sitter_jsdoc
from dataclasses import dataclass
from tree_sitter import Language, Node, Parser

TAB = "    "

# We use JSDoc since it is available on PyPI and has similar syntax
DOXYGEN_LANGUAGE = Language(tree_sitter_jsdoc.language(), "doxygen")
CPP_LANGUAGE = Language(tree_sitter_cpp.language(), "cpp")

# Initialize parser
cpp_parser = Parser()
cpp_parser.set_language(CPP_LANGUAGE)  # Needed in 0.21

doxygen_parser = Parser()
doxygen_parser.set_language(DOXYGEN_LANGUAGE)


class_query = CPP_LANGUAGE.query("""
((comment) @comment
    .
    (class_specifier
        name: (type_identifier) @name
        body: (field_declaration_list)
        ) @class
        )
""")

method_query = CPP_LANGUAGE.query("""
((comment) @comment
    .
    (field_declaration
        (storage_class_specifier)? @storage_class
        declarator: (function_declarator
            declarator: (field_identifier) @name
            parameters: (parameter_list)? @parameters
        )
        ))
""")

function_query = CPP_LANGUAGE.query("""
((comment) @comment
 .
 (declaration
     (storage_class_specifier)? @storage_class
     declarator: (function_declarator
         declarator: (identifier) @name
         parameters: (parameter_list)? @parameters
     )
    ))
""")

# Unfortunately, tree-sitter does not allow node type alternations
parameter_query = CPP_LANGUAGE.query("""
([(parameter_declaration
	[(qualified_identifier) (primitive_type) (type_identifier) (template_type)] @type
	[(reference_declarator) (pointer_declarator) (identifier)]? @identifier
)
(optional_parameter_declaration
	[(qualified_identifier) (primitive_type) (type_identifier) (template_type)] @type
	[(reference_declarator) (pointer_declarator) (identifier)]? @identifier
    default_value: (_) @default_value
)])
""")


@dataclass
class FunctionDoc:
    doc: str
    python_name: Optional[str]


def build_function_docstring(node: Node):
    brief = ""
    params = []
    ret = ""
    doc = ""
    python_name = None

    for n in node.children:
        match n.type:
            case "description":
                brief = n.text.decode("utf-8").replace("*", "").replace("\n", "\\n")
            case "tag":
                match n.children[0].text.decode("utf-8"):
                    case "@param":
                        params.append(
                            (
                                n.children[1].text.decode("utf-8"),
                                n.children[2]
                                .text.decode("utf-8")
                                .replace("*", "")
                                .replace("\n", "\\n"),
                            )
                        )
                    case "@return":
                        ret = (
                            n.children[1]
                            .text.decode("utf-8")
                            .replace("*", "")
                            .replace("\n", "\\n")
                        )
                    case "@python_name":
                        python_name = n.children[1].text.decode("utf-8")

    doc += brief

    if params:
        params_text = [f"{i}: {d}" for (i, d) in params]
        doc += r"\n\nArgs:\n" + TAB + (r"\n" + TAB).join(params_text)

    if ret:
        doc += r"\n\nReturns: " + ret

    return FunctionDoc(doc, python_name)


def build_function(
    match: Dict[str, Node | List[Node]],
    overload: bool = True,
    class_name: Optional[str] = None,
) -> str:
    """Build a function or method declaration."""

    comment_tree = doxygen_parser.parse(match["comment"].text)
    brief = func_doc_brief_query.matches(comment_tree.root_node)

    if not brief:
        return ""

    function_doc = build_function_docstring(comment_tree.root_node)
    doc = function_doc.doc
    python_name = function_doc.python_name

    params: list[tuple[str, str, Optional[str]]] = []
    if "parameters" in match:
        for param_match in parameter_query.matches(match["parameters"]):
            param_type = param_match[1]["type"].text.decode("utf-8")
            identifier = param_match[1]["identifier"].text.decode("utf-8")
            if len(identifier_split := identifier.split(" ")) > 1:
                param_type += identifier_split[0]
                identifier = identifier_split[1]

            params.append(
                (
                    param_type,
                    identifier,
                    param_match[1]["default_value"].text.decode("utf-8")
                    if "default_value" in param_match[1]
                    else None,
                )
            )

    params_text = ""
    for param in params:
        params_text += f', "{param[1]}"_a'
        if param[2]:
            params_text += f" = {param[2]}"

    fn_name = match["name"].text.decode("utf-8")
    bind_name = fn_name
    if python_name:
        bind_name = python_name

    def_fn = "def"
    if fn_name.startswith("get"):
        def_fn = "def_prop_ro"
        bind_name = fn_name[4:]
    elif "storage_class" in match:
        storage_class = match["storage_class"].text.decode("utf-8")
        match storage_class:
            case "static":
                def_fn = "def_static"

    # __ is reserved in C++
    if fn_name.startswith("magic"):
        fn_name = "__" + fn_name[6:] + "__"

    ref = "&" + (class_name + "::" if class_name else "") + fn_name

    if overload:
        ref = f'nb::overload_cast<{", ".join([p[0] for p in params])}>({ref})'

    return f'.{def_fn}("{bind_name}", {ref}{params_text}, "{doc}")'


query_class_comment = DOXYGEN_LANGUAGE.query("""
(tag
    (tag_name) @tag_name
    (identifier)? @identifier
    (description)? @description
    (type)? @type
) """)

func_doc_brief_query = DOXYGEN_LANGUAGE.query("""
((description) @description)
""")


# Match classes
def match_classes(node: Node) -> str:
    output = ""

    for match in class_query.matches(node):
        class_name = match[1]["name"].text.decode("utf-8")
        class_hierarchy = [class_name]

        if "comment" in match[1]:
            comment = match[1]["comment"]
            comment_tree = doxygen_parser.parse(comment.text)
            for comment_match in query_class_comment.matches(comment_tree.root_node):
                match comment_match[1]["tag_name"].text.decode("utf-8"):
                    case "@inherit":
                        class_hierarchy.extend(
                            comment_match[1]["description"]
                            .text.decode("utf-8")
                            .strip()
                            .split(", ")
                        )
                ...

        class_output = f'nb::class_<{", ".join(class_hierarchy)}>(m, "{class_name}")'

        fn_matches = method_query.matches(match[1]["class"])
        fn_names = [match[1]["name"].text for match in fn_matches]
        fn_defs = [
            f"\n{TAB}{TAB}"
            + build_function(
                match[1], fn_names.count(match[1]["name"].text) > 1, class_name
            )
            for match in fn_matches
        ]
        class_output += "".join(fn_defs) + ";"

        output += class_output

    return output


def generate_free_functions(node: Node) -> str:
    # for match in function_query.matches(node):
    #     output += build_function(match[1])

    fn_matches = function_query.matches(node)
    fn_names = [match[1]["name"].text for match in fn_matches]
    fn_defs = [
        "m"
        + build_function(match[1], fn_names.count(match[1]["name"].text) > 1, None)
        + ";"
        for match in fn_matches
    ]

    output = f"\n{TAB}".join(fn_defs)
    return output


def generate_enums(node: Node) -> str:
    enum_query = CPP_LANGUAGE.query("""((comment)
                            . 
                          (enum_specifier
                            name: (type_identifier) @name
                            body: (enumerator_list
                                    (enumerator)+)
                                    @enum_list))""")

    matches = enum_query.matches(node)
    enums = []
    for match in matches:
        name = match[1]["name"].text.decode("utf-8")
        enumerators: list[tuple[str, str]] = []
        enumerator_nodes = [
            e for e in match[1]["enum_list"].children if e.type == "enumerator"
        ]
        for enumerator_node in enumerator_nodes:
            entry_name = enumerator_node.children[0].text.decode("utf-8")
            value = (
                enumerator_node.children[1].text.decode("utf-8")
                if len(enumerator_node.children) == 2
                else "auto()"
            )
            enumerators.append((entry_name, value))

        enums.append(
            f'{TAB}nb::enum_<{name}>(m, "{name}")'
            + "".join(
                f'\n{TAB}{TAB}.value("{n}", {name}::{n})' for (n, v) in enumerators
            )
            + ";"
        )

    return "\n\n".join(enums)


def build_header(header_name: str, source_code: str) -> str:
    tree = cpp_parser.parse(bytes(source_code, "utf8"))

    free_functions = generate_free_functions(tree.root_node)

    enums = generate_enums(tree.root_node)

    return f"""#pragma once
// This file was autogenerated. Do not edit. //
#include "{header_name}.h"

void bind_{header_name.lower()}(nb::module_ &m)
{{
    // Classes
    {match_classes(tree.root_node)}

    // Functions
    {free_functions}

    // Enums
{enums}
}};
"""


def main():
    parser = argparse.ArgumentParser(description="Input headers")
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        required=True,
        help="the directory where output files will be saved",
    )
    parser.add_argument(
        "files", metavar="F", type=str, nargs="+", help="a file to be processed"
    )
    args = parser.parse_args()

    for file_path in args.files:
        with open(file_path, "r") as f:
            path = Path(file_path)
            source_code = f.read()
            code = build_header(path.stem, source_code)

            output_file = Path(args.output.strip()) / f"bind_{path.stem}.h"

            with open(output_file, "w") as f:
                f.write(code)


if __name__ == "__main__":
    main()
