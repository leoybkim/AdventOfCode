import hashlib


def read_file(file_path: str) -> str:
    with open(file_path) as input_file:
        return input_file.read()


def find_number(raw_input: str, zeros=5) -> int:
    number = 0
    while True:
        test = hashlib.md5((raw_input + str(number)).encode("utf-8"))
        hex_str = test.hexdigest()
        if hex_str[0:zeros] == "0" * zeros:
            break
        number += 1
    return number


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Lowest positive number that produce correct MD5 hash: {find_number(file)}")
    print(f"Lowest positive number that produce correct MD5 hash with 6 zeros: {find_number(file, zeros=6)}")
