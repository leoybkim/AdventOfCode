from itertools import groupby

from utils.input_reader import read_file


def look_and_say(sequence: str, itr: int) -> str | int:
    """
    :param sequence: previous sequence
    :param itr: number of times to repeat the generation of look-and-say sequence
    :return new look-and-say sequence
    """
    temp = []
    if itr > 0:
        for key, group in groupby(sequence):
            temp.append("".join(group))
        new_sequence = []
        for item in temp:
            new_sequence.append(str(len(item)))
            new_sequence.append(item[0])
        return look_and_say("".join(new_sequence), itr - 1)
    else:
        return len(sequence)


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Length of the sequence after 40 iteration of look-and-say: {look_and_say(file, 40)}")
    print(f"Length of the sequence after 50 iteration of look-and-say: {look_and_say(file, 50)}")
