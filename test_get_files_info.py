from functions.get_files_info import get_files_info


def test_get_files_info():
    test_cases = [("calculator", "."), ("calculator", "pkg"), ("calculator", "/bin"), ("calculator", "../")]
    for test_case in test_cases:
        file_info = get_files_info(*test_case)
        print(f"Result for '{test_case[1]}' directory:\n {file_info}")
    
if __name__ == "__main__":
    test_get_files_info()