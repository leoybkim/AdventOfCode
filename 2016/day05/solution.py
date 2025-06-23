import hashlib


def read_file(file_path: str) -> str:
    with open(file_path) as input_file:
        return input_file.read()


def find_password(raw_input: str) -> str:
    door_id = raw_input.strip()
    password = []
    i = 0
    while len(password) < 8:
        hex_digest = hashlib.md5((door_id + str(i)).encode()).hexdigest()
        if hex_digest[:5] == "00000":
            password.append(hex_digest[5])
        i += 1
    return "".join(password)


def find_password2(raw_input: str) -> str:
    door_id = raw_input.strip()
    password = [None] * 8
    character_found = 0
    i = 0
    while character_found < 8:
        hex_digest = hashlib.md5((door_id + str(i)).encode()).hexdigest()
        if hex_digest[:5] == "00000":
            if hex_digest[5].isdigit() and 0 <= int(hex_digest[5]) < 8 and password[int(hex_digest[5])] is None:
                password[int(hex_digest[5])] = hex_digest[6]
                character_found += 1
        i += 1
    return "".join(password)


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"The password is: {find_password(file)}")
    print(f"The new password is: {find_password2(file)}")
