from setuptools import setup, find_packages

setup(
    name="code-generator-odin",
    version="0.1.2",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "generate-code=code_generator.cli:main",
        ],
    },
    author="Khai Hoang",
    author_email="khaihq@gfigroup.io",
    description="A flexible source code generator with fixed structure templates",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords="code generator, template, python",
    url="https://github.com/odin-hoang/code-generator",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
)
