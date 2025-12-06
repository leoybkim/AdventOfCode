from utils.input_reader import read_file


def decompressed_length(input_str: str, s=0, e=None, part2=False) -> int:
    new_input_str_len = 0
    in_data_section = True
    in_char_count_mode = True
    char_count_str = []
    repeat_count_str = []
    N = 0
    if e is None:
        e = len(input_str)

    for i in range(s, e):
        if N > 0:
            # skip data section covered by previous marker
            N -= 1
        else:
            if in_data_section:
                # look for marker signs which is opening brace
                if input_str[i] == "(":
                    # entering marker section
                    in_data_section = False
                else:
                    new_input_str_len += 1
            else:
                if in_char_count_mode:
                    # look for x which enters char repeat mode
                    if input_str[i] != "x":
                        char_count_str.append(input_str[i])
                    else:
                        in_char_count_mode = False
                else:
                    if input_str[i] != ")":
                        repeat_count_str.append(input_str[i])
                    else:
                        # entering data section
                        in_data_section = True
                        in_char_count_mode = True

                        # you now have info on N characters to repeat M times
                        N = int("".join(char_count_str))
                        M = int("".join(repeat_count_str))

                        if part2:
                            new_input_str_len += decompressed_length(input_str, i + 1, i + 1 + N, part2=part2) * M
                        else:
                            new_input_str_len += N * M

                        char_count_str = []
                        repeat_count_str = []
    return new_input_str_len


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Decompressed length of file: {decompressed_length(file)}")
    print(f"Decompressed length of file with improved format: {decompressed_length(file, part2=True)}")
