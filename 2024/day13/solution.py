import math
import re
from typing import List

from utils.input_reader import read_file


def format_data(raw_data: str) -> List[dict]:
    games = []
    a = re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
    b = re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
    prize = re.compile(r"Prize: X=(\d+), Y=(\d+)")
    for section in raw_data.split("\n\n"):
        lines = section.split("\n")
        a_match = a.search(lines[0])
        b_match = b.search(lines[1])
        prize_match = prize.search(lines[2])

        game = {
            "A": (int(a_match.group(1)), int(a_match.group(2))),
            "B": (int(b_match.group(1)), int(b_match.group(2))),
            "prize": (int(prize_match.group(1)), int(prize_match.group(2)))
        }
        games.append(game)
    return games


def find_solution(game: dict) -> tuple:
    """
    Solve m and n for two linear equations:
    prize_x = A_x * m + B_x * n
    prize_y = A_y * m + B_y * n
    @param game: Game object
                 A = (x, y)
                 B = (x, y)
                 prize = (x coordinate, y coordinate)
    @return: Number of presses for button A, Number of presses for button B to get to prize
    """
    m = n = None
    if ((game["prize"][0] * game["A"][1] - game["prize"][1] * game["A"][0]) %
        (game["B"][0] * game["A"][1] - game["B"][1] * game["A"][0])) == 0:
        n = ((game["prize"][0] * game["A"][1] - game["prize"][1] * game["A"][0]) //
             (game["B"][0] * game["A"][1] - game["B"][1] * game["A"][0]))
    if n is not None and (game["prize"][0] - game["B"][0] * n) % game["A"][0] == 0:
        m = (game["prize"][0] - game["B"][0] * n) // game["A"][0]
    return m, n


def calculate_tokens(raw_input: str, offset=0) -> int:
    games = format_data(raw_input)
    tokens = 0
    for game in games:
        gcd_x = math.gcd(game["A"][0], game["B"][0])
        gcd_y = math.gcd(game["A"][1], game["B"][1])
        if offset > 0:
            game["prize"] = (game["prize"][0] + offset, game["prize"][1] + offset)
        if game["prize"][0] % gcd_x == 0 and game["prize"][1] % gcd_y == 0:
            # Game is solvable based on Bézout's identity
            a_presses, b_presses = find_solution(game)
            if a_presses is not None and b_presses is not None:
                if offset > 0:
                    if 0 <= a_presses and 0 <= b_presses:
                        tokens += (3 * a_presses + b_presses)
                else:
                    if 0 <= a_presses <= 100 and 0 <= b_presses <= 100:
                        tokens += (3 * a_presses + b_presses)

    return tokens


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Fewest tokens needed to spend to win all possible prizes: {calculate_tokens(file)}")
    print(f"Fewest tokens needed to spend to win all possible prizes: {calculate_tokens(file, offset=10000000000000)}")
