from functions.get_file_content import get_file_content


def test_get_file_content():
    test_cases = [("calculator", "lorem.txt"), ("calculator", "main.py"), ("calculator", "pkg/calculator.py"), ("calculator", "/bin/cat"), ("calculator", "pkg/does_not_exist.py")]
    for test_case in test_cases:
        file_content = get_file_content(*test_case)
        print(f"Result for '{test_case[1]}' file:\n {file_content}")

if __name__ == "__main__":
    test_get_file_content()