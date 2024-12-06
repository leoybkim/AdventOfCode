from collections import defaultdict
from typing import List


def read_file(input_file_path: str) -> str:
    with  open(input_file_path) as input_file:
        return input_file.read()


def format_data(raw_data: str) -> tuple[defaultdict, List[List[int]]]:
    """
    Format the input file
    :param raw_data: Original input
    :return: Tuple of objects extracted from input: page ordering rules and list of updates
    """
    rules = defaultdict(list)
    updates = []
    for line in raw_data.split():
        if "|" in line:
            num1, num2 = map(int, line.split("|"))
            rules[num2].append(num1)
        else:
            updates.append(list(map(int, line.split(','))))
    return rules, updates


def find_swap(n: int, rules: defaultdict, update: List[int]) -> int | None:
    """
    Checks if page can be produced based on the page ordering rule.
    If the page is in incorrect order, return the page that it needs to swap in position with from the update list
    :param n: Page to produce
    :param rules: Page ordering rule
    :param update: List of pages to produce after to the current page
    :return: None if page is in order, otherwise return the page it needs to swap with
    """
    if len(rules[n]) > 0:
        for m in rules[n]:
            if m in update:
                return m
    return None


def find_updates(rules: defaultdict, updates: List[List[int]], correct_order=True) -> List[List[int]]:
    """
    From the given updates return the correct set of updates depending on the query
    :param rules: Page ordering rules
    :param updates: List of pages to produce in each update
    :param correct_order: Flag to indicate whether to return correctly ordered updates or incorrectly ordered updates
    :return: Correctly ordered or incorrectly ordered updates depending on the flag provided
    """
    correct_updates = []
    incorrect_updates = []
    for update in updates:
        correct = True
        for i, n in enumerate(update):
            swap = find_swap(n, rules, update[i + 1:])
            if swap is not None:
                correct = False
                incorrect_updates.append(update)
                break

        if correct:
            correct_updates.append(update)

    return correct_updates if correct_order else incorrect_updates


def correct_update_order(rules: defaultdict, incorrect_updates: List[List[int]]) -> List[List[int]]:
    """
    Reorder the incorrect updates by following the page ordering rules
    :param rules: Page ordering rule
    :param incorrect_updates: List of incorrect updates
    :return: List of corrected updates
    """
    for update in incorrect_updates:
        for i in range(len(update)):
            swap = find_swap(update[i], rules, update[i + 1:])
            while swap is not None:
                j = update.index(swap)
                update[i], update[j] = update[j], update[i]
                swap = find_swap(update[i], rules, update[i + 1:])
    return incorrect_updates


def sum_middle_pages(updates: List[List[int]]) -> int:
    """
    Sum up middle index pages from all the update list
    :param updates: List of updates
    :return: Sum of middle pages
    """
    s = 0
    for update in updates:
        if len(update) % 2:
            m = len(update) // 2
            s += update[m]
    return s


def sum_correct_ordered_middle_pages(raw_data: str) -> int:
    """
    Part 1
    :param raw_data: input file
    :return: Sum of middle page number of correctly ordered updates
    """
    rules, updates = format_data(raw_data)
    correct_updates = find_updates(rules, updates, correct_order=True)
    return sum_middle_pages(correct_updates)


def sum_incorrect_ordered_middle_pages_after_reordering(raw_data: str) -> int:
    """
    Part 2
    :param raw_data: input file
    :return: Sum of middle page numbers after correctly ordering the incorrect update list
    """
    rules, updates = format_data(raw_data)
    incorrect_updates = find_updates(rules, updates, correct_order=False)
    corrected_updates = correct_update_order(rules, incorrect_updates)
    return sum_middle_pages(corrected_updates)


if __name__ == "__main__":
    file = read_file("input.txt")
    print(f"Sum of correctly-ordered updates' middle pages: {sum_correct_ordered_middle_pages(file)}")
    print(f"Sum of incorrectly-ordered updates' middle pages after reordering: "
          f"{sum_incorrect_ordered_middle_pages_after_reordering(file)}")
