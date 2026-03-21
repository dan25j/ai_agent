from functions.write_file import write_file


def test_write_file():
    test_cases = [("calculator", "lorem.txt", "wait, this isn't lorem ipsum"), ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"), ("calculator", "/tmp/temp.txt", "this should not be allowed")]
    for test_case in test_cases:
        result = write_file(*test_case)
        print(f"Result for '{test_case[1]}' file:\n {result}")

if __name__ == "__main__":
    test_write_file()