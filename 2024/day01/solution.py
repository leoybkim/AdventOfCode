from collections import defaultdict

from utils.input_reader import read_file


def find_total_distance(data: str) -> int:
    """
    Read the input file
    Separate the left and right columns and sort the two list in ascending order
    Iterate through the list and sum up the distance between the two values
    :param data: input file data
    :return: Total distance between the left and right list
    """
    total_distance = 0
    list1 = []
    list2 = []

    for line in data.splitlines():
        num1, num2 = map(int, line.split())  # Split the line at whitespace and convert to integer
        list1.append(num1)
        list2.append(num2)

    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        total_distance += abs(list2[i] - list1[i])

    return total_distance


def find_similarity_score(data: str) -> int:
    """
    Separate the left and right columns
    Insert left value into a List and record right value as a key to a map with the initial value of 1
    Increment the value of the map each time key is found on the right column
    Iterate through the left column list and calculate the similarity score
    :param data: input file data
    :return: Total similarity score
    """
    total_score = 0
    list1 = []
    map2 = defaultdict(int)

    for line in data.splitlines():
        num1, num2 = map(int, line.split())  # Split the line at whitespace and convert to integer
        list1.append(num1)
        map2[num2] += 1  # Increment the value each time num2 is found
    for num in list1:
        total_score += num * map2.get(num, 0)

    return total_score


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Total distance is: {find_total_distance(file)}")
    print(f"Total similarity score is: {find_similarity_score(file)}")
