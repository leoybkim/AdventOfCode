from itertools import groupby


def read_file(file_path: str) -> str:
    with open(file_path) as input_file:
        return input_file.read()


def validate_password(password: str) -> bool:
    """
    Checks if provided password passes the password policy
    1. Exactly 8 lowercase letters
    2. Must include one increasing straight of at least 3 letters
    3. May not contain the letters i, o, or l
    4. Must contain at least two different non-overlapping pairs of letters
    :param password: password under test
    :returns: whether the provided password passes the policy or not
    """

    # rule 1
    if len(password) != 8:
        return False
    if password.lower() != password:
        return False

    # rule 2
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    contains = False
    for i in range(len(alphabets) - 2):
        contains = True if alphabets[i:i + 3] in password else False
        if contains:
            break
    if not contains:
        return False

    # rule 3
    for c in password:
        if c in ["i", "o", "l"]:
            return False

    # rule 4
    pair1 = None
    pair2 = None
    for k, group in groupby(password):
        if len(list(group)) >= 2:
            if not pair1:
                pair1 = k
            elif pair1 != k:
                pair2 = k
                break
    if not pair1 or not pair2:
        return False

    return True


def generate_password(current_password: str, iteration=1) -> str:
    new_password = None
    while iteration > 0:
        valid = False
        while not valid:
            new_password = increment_string(current_password)
            valid = validate_password(new_password)
            current_password = new_password
        iteration -= 1
    return new_password


def increment_string(current_string: str) -> str:
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    n = len(current_string)
    s_list = list(current_string)
    for i in range(n - 1, -1, -1):
        char = s_list[i]
        char_idx = alphabets.index(char)
        if char_idx < len(alphabets) - 1:
            # increment if not the last character in the alphabet
            s_list[i] = alphabets[char_idx + 1]
            return "".join(s_list)  # Return the incremented string
        else:
            # set it to the first alphabet and carry over
            s_list[i] = alphabets[0]
            if i == 0:
                # need to also prepend the first character if leftmost character
                s_list.insert(0, alphabets[0])
                return "".join(s_list)
    return "".join(s_list)


if __name__ == "__main__":
    input = read_file("inputs/input.txt")
    print(f"Santa's new password is: {generate_password(input)}")
    print(f"Santa's next new password is: {generate_password(input, 2)}")
