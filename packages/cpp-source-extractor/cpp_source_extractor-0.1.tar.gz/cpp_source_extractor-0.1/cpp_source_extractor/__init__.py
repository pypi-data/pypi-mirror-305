import clang.cindex

# re-export the public interface
from .extractor import _extract_function_by_name, _extract_function_by_line_number


def set_libclang_path(libclang_path: str):
    """
    Set the path to the libclang.so file.
    """
    clang.cindex.Config.set_library_file(libclang_path)

# Public interfaces


def extract_function_by_name(func_name: str, file_path: str, extra_args: list[str] = [], database: str | None = None) -> list[tuple[int, str]]:
    return _extract_function_by_name(file_path, func_name, extra_args, database)


def extract_function_by_line_number(line_number: int, file_path: str, extra_args: list[str] = [], database: str | None = None) -> list[tuple[int, str]]:
    return _extract_function_by_line_number(file_path, line_number, extra_args, database)
