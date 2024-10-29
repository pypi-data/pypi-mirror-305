# C++ Source Extractor

C++ Source Extractor is a Python library designed to extract C++ function implementations from source code files using the Clang `cindex` module.

## Features

- Extract functions by name
- Extract functions using regular expressions
- Extract functions by line number

## Installation

To use this library, ensure you have Python installed along with the `clang` library. You can install `clang` using pip:

```bash
pip install clang
```

## Usage

### Extract a Function by Name

You can extract a typical C-style function by specifying its name.

```python
from cpp_source_extractor import extract_function_by_name

code = extract_function_by_name("main", "main.cpp")
print(code)
```

### Extract a Function by Line Number

If you have the line number (from a debugger or stack trace) where the function is located, you can extract it using this method. This is recommended as it avoids issues like name mangling.

Note: The line number can be within the body of the function, not necessarily the line where the function is defined.

```python
from cpp_source_extractor import extract_function_by_line_number

code = extract_function_by_line_number(10, "main.cpp")
print(code)
```

### Add semantic information

Extracting functions wrapped in preprocessor directives can be challenging, as shown in the example below:

```c
#ifdef __os_linux__
void foo() {
    // ...
}
#elif __os_macos__
void foo() {
    // ...
}
#endif
```

Here, the function foo is defined differently based on the operating system configuration. To ensure you extract the correct version of the function, you have two options:

1. **Use Compile Arguments**: Specify the relevant macro definitions as compile arguments (e.g., `-D__os_linux__` or `-D__os_macos__`) when extracting functions:

```python
code = extract_function_by_name("foo", "main.cpp", extra_args=["-D__os_linux__"])
print(code)
```

2. **Use a Compilation Database**: Provide the path to a [JSON Compilation Database](https://clang.llvm.org/docs/JSONCompilationDatabase.html), which contains the necessary build information:

```python
code = extract_function_by_name("foo", "main.cpp", database="/path/to/compile_commands.json")
print(code)
```

You can generate a compilation database using CMake:

```bash
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON .
```

Or, for Make-based projects, you can use [bear](https://github.com/rizsotto/Bear) to generate the compilation database.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.