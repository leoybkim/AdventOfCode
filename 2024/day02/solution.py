from typing import List


def is_safe(report: List[int]) -> bool:
    """
    Checks for condition of the report and returns the safety status
    Report counts as safe if both of the following are true:
    - The levels are either all increasing or all decreasing
    - Any two adjacent levels differ by at least 1 and at most 3
    :param report: Individual line of report from input to be checked
    :return: Safety of the report
    """
    sorting = report[len(report) - 1] - report[0]  # Positive means ASC, negative means DESC
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if not (sorting * diff > 0 and 1 <= abs(diff) <= 3):
            # If the direction has not changed pos x pos or neg x neg should return a positive number
            return False
    return True


def num_safe_reports(input_file_path: str, dampener=0) -> int:
    """
    Read the input file
    Extract each line as List of ints which represents a report
    Determine if each report is safe, increment count if safe
    Allow removal for one bad level before checking safety if dampener is set to 1
    :param dampener: Tolerance for one bad level
    :param input_file_path: Relative path to the input
    :return: Number of safe reports
    """
    count = 0
    with (open(input_file_path, "r") as input_file):
        for line in input_file:
            report = list(map(int, line.split()))  # Split the line at whitespace and convert to List of ints
            if dampener:
                # Allow for removal of one bad level. Iterate through each level and check if sublist is safe without it.
                for i in range(len(report)):
                    sublist_report = report[:i] + report[i + 1:]  # Remove one level at index i and create a sublist
                    if is_safe(sublist_report):
                        count += 1
                        break
            else:
                if is_safe(report):
                    count += 1
    return count


if __name__ == "__main__":
    print(f"Total number of safe reports: {num_safe_reports("input.txt")}")
    print(f"Total number of safe reports (with dampener): {num_safe_reports("input.txt", dampener=1)}")
