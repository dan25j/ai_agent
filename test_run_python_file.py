from functions.run_python_file import run_python_file


def test_run_python_file():
    test_cases = [("calculator", "main.py"), ("calculator", "main.py", ["3 + 5"]), ("calculator", "tests.py"), ("calculator", "../main.py"), ("calculator", "nonexistent.py"), ("calculator", "lorem.txt")]
    for test_case in test_cases:
        file_info = run_python_file(*test_case)
        print(f"Result for '{test_case[1]}' file:\n {file_info}")


if __name__ == "__main__":
    test_run_python_file()