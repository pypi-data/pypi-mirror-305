#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path
from . import __version__


class CodeGenerator:
    def __init__(self):
        self.indentation = "    "
        self.class_template = """class {class_name}:
{docstring}
{class_content}"""

        self.method_template = """{indent}def {method_name}(self{params}):
{indent}{docstring}
{method_content}"""

        self.property_template = """{indent}@property
{indent}def {property_name}(self):
{indent}{docstring}
{method_content}"""

    def generate_docstring(self, content, indent_level=0):
        indent = self.indentation * indent_level
        return f'{indent}"""\n{indent}{content}\n{indent}"""'

    def generate_class(self, class_name, docstring="", methods=None, properties=None):
        formatted_docstring = self.generate_docstring(docstring, indent_level=1)

        methods_code = []
        if methods:
            for method in methods:
                method_code = self.generate_method(**method)
                methods_code.append(method_code)

        properties_code = []
        if properties:
            for prop in properties:
                prop_code = self.generate_property(**prop)
                properties_code.append(prop_code)

        class_content = "\n\n".join(properties_code + methods_code)
        if class_content:
            class_content = "\n" + class_content

        return self.class_template.format(
            class_name=class_name,
            docstring=formatted_docstring,
            class_content=class_content,
        )

    def generate_method(
        self, name, params=None, docstring="", content=None, indent_level=1
    ):
        indent = self.indentation * indent_level

        formatted_params = ""
        if params:
            formatted_params = ", " + ", ".join(params)

        formatted_docstring = self.generate_docstring(
            docstring, indent_level=indent_level + 1
        )

        if content is None:
            content = [f"{indent}{self.indentation}pass"]
        else:
            content = [f"{indent}{self.indentation}{line}" for line in content]

        method_content = "\n".join(content)

        return self.method_template.format(
            indent=indent,
            method_name=name,
            params=formatted_params,
            docstring=formatted_docstring,
            method_content=method_content,
        )

    def generate_property(self, name, docstring="", content=None, indent_level=1):
        indent = self.indentation * indent_level

        formatted_docstring = self.generate_docstring(
            docstring, indent_level=indent_level + 1
        )

        if content is None:
            content = [f"{indent}{self.indentation}pass"]
        else:
            content = [f"{indent}{self.indentation}{line}" for line in content]

        method_content = "\n".join(content)

        return self.property_template.format(
            indent=indent,
            property_name=name,
            docstring=formatted_docstring,
            method_content=method_content,
        )


def load_template(template_path):
    """Load class template from JSON file."""
    with open(template_path, "r") as f:
        return json.load(f)


def save_output(content, output_path):
    """Save generated code to file."""
    with open(output_path, "w") as f:
        f.write(content)


def main():
    parser = argparse.ArgumentParser(
        description="Generate Python source code from template"
    )
    parser.add_argument(
        "-t", "--template", type=str, required=True, help="Path to JSON template file"
    )
    parser.add_argument(
        "-o", "--output", type=str, help="Output file path (defaults to stdout)"
    )
    parser.add_argument(
        "--indent",
        type=int,
        default=4,
        help="Number of spaces for indentation (default: 4)",
    )

    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}"
    )

    args = parser.parse_args()

    # Validate template path
    template_path = Path(args.template)
    if not template_path.exists():
        print(f"Error: Template file '{args.template}' not found", file=sys.stderr)
        sys.exit(1)

    try:
        # Load template
        template = load_template(template_path)

        # Generate code
        generator = CodeGenerator()
        generator.indentation = " " * args.indent
        generated_code = generator.generate_class(**template)

        # Output
        if args.output:
            save_output(generated_code, args.output)
            print(f"Code generated successfully: {args.output}")
        else:
            print(generated_code)

    except json.JSONDecodeError:
        print(
            f"Error: Invalid JSON in template file '{args.template}'", file=sys.stderr
        )
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Missing required field in template: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
