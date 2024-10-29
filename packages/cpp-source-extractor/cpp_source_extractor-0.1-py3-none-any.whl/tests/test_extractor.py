from cpp_source_extractor import extract_function_by_name, extract_function_by_line_number


def test_extract_function_by_name():
    code = extract_function_by_name("main", "tests/testcases/simple.c")
    assert code == [
        (1, "int main() {"),
        (2, "    return 0;"),
        (3, "}")
    ]


def test_extract_function_by_line_number():
    code = extract_function_by_line_number(
        857, "tests/testcases/libxml2/globals.c", extra_args=["-DLIBXML_THREAD_ENABLED", "-DHAVE_POSIX_THREADS", "-DUSE_TLS", "-DXML_THREAD_LOCAL"])
    assert code[:2] == [
        (856, "static xmlGlobalStatePtr"),
        (857, "xmlGetThreadLocalStorage(int allowFailure) {")
    ]
