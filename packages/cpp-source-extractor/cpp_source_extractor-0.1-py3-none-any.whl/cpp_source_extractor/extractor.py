import clang.cindex
import os


def _find_function_definition_by_name(node: clang.cindex.Cursor, func_name: str) -> clang.cindex.Cursor | None:
    """
    Recursively search for the function definition in the AST.
    """
    if node.kind in {clang.cindex.CursorKind.FUNCTION_DECL, clang.cindex.CursorKind.CXX_METHOD} and node.spelling == func_name and node.is_definition():
        return node
    for child in node.get_children():
        result = _find_function_definition_by_name(child, func_name)
        if result is not None:
            return result
    return None


def _find_function_definition_by_line_number(node: clang.cindex.Cursor, line_number: int) -> clang.cindex.Cursor | None:
    """
    Recursively search for the function definition in the AST by line number.
    """
    if node.extent.start.line <= line_number <= node.extent.end.line:
        if node.kind in {clang.cindex.CursorKind.FUNCTION_DECL, clang.cindex.CursorKind.CXX_METHOD} and node.is_definition():
            return node

    for child in node.get_children():
        result = _find_function_definition_by_line_number(child, line_number)
        if result is not None:
            return result
    return None


def _extract_node_source(node: clang.cindex.Cursor) -> list[tuple[int, str]]:
    """
    Extract the source code for the function from the AST node.
    Return an array of tuples containing line number and content.
    """
    start = node.extent.start
    end = node.extent.end
    with open(start.file.name, 'r') as f:
        lines = f.readlines()
        func_lines = lines[start.line - 1:end.line]
        result = [(i + start.line, line.rstrip())
                  for i, line in enumerate(func_lines)]
    return result


def _get_compile_args(file_path: str, database: str) -> list[str]:
    """
    Get the compile args from the compilation database.
    """
    if not os.path.exists(database):
        raise FileNotFoundError(f"Compilation database {database} not found.")
    compdb = clang.cindex.CompilationDatabase.fromDirectory(database)
    commands = compdb.getCompileCommands(file_path)

    compile_args = []
    for command in commands:
        for arg in command.arguments:
            # we only keep args starting with '-D', which are the preprocessor definitions
            if arg.startswith('-D'):
                compile_args.append(arg)
    return compile_args


def _create_translation_unit(file_path: str, extra_args: list[str], database: str | None) -> clang.cindex.TranslationUnit:
    """
    Create a translation unit from the source file. If the file does not exist, raise a FileNotFoundError.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Source file {file_path} not found. Current working directory: {os.getcwd()}")
    index = clang.cindex.Index.create()

    compile_args = ['-x', 'c++', '-std=c++11']
    if database:
        compile_args.extend(_get_compile_args(file_path, database))
    if extra_args:
        compile_args.extend(extra_args)

    translation_unit = index.parse(file_path, args=compile_args)
    if translation_unit is None:
        raise RuntimeError(f"Unable to parse the source file {file_path}.")
    return translation_unit


def _extract_function_by_name(file_path: str, func_name: str, extra_args: list[str], database: str) -> list[tuple[int, str]] | None:
    """
    Get the implementation of the specified function from the source file.
    """
    translation_unit = _create_translation_unit(
        file_path, extra_args, database)
    function_node = _find_function_definition_by_name(
        translation_unit.cursor, func_name)
    if function_node is None:
        print(f"[!] Function {
              func_name} not found in the source file {file_path}.")
        return None
    function_source = _extract_node_source(function_node)
    return function_source


def _extract_function_by_line_number(file_path: str, line_number: int, extra_args: list[str], database: str | None) -> list[tuple[int, str]] | None:
    """
    Get the implementation of the specified function from the source file using a line number.
    """
    translation_unit = _create_translation_unit(
        file_path, extra_args, database)
    function_node = _find_function_definition_by_line_number(
        translation_unit.cursor, line_number)
    if function_node is None:
        print(f"[!] Function at line {
              line_number} not found in the source file {file_path}.")
        return None
    function_source = _extract_node_source(function_node)
    return function_source
