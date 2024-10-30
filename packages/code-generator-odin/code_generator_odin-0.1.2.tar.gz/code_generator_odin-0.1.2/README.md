# Code Generator Odin

A flexible source code generator with fixed structure templates.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Generate code snippets for various programming languages.
- Create project templates for quick setup.
- Customize boilerplate code to fit your needs.

## Installation

To install the Code Generator Odin, clone the repository and install the dependencies:

```sh
git clone https://github.com/odin-hoang/code-generator.git
cd code-generator
pip install .
```

For development, you can install the package with testing dependencies:

```sh
pip install -e .[test]
```

## Usage

To generate a code snippet, run the following command:

```sh
generate-code -t path/to/template.json -o path/to/output.py
```

**Arguments**

- `-t`, `--template`: Path to the JSON template file (required).
- `-o`, `--output`: Output file path (defaults to stdout).
- `--indent`: Number of spaces for indentation (default: 4).

## Development

**Running Tests**

```sh
pytest tests/
```

The tests are automatically run on each push and pull request to the main branch using GitHub Actions. See the tests.yml for more details.

# Contributing

We welcome contributions! Please read our contributing guidelines for more details.

# License

This project is licensed under the MIT License. See the LICENSE file for more information.
