from collections import Counter
from itertools import combinations_with_replacement
from re import match


def read_file(file_path: str) -> str:
    with open(file_path) as input_file:
        return input_file.read()


def parse_info(raw_input: str) -> dict:
    """
    Returns the parsed information from recipe properties
    :param raw_input: raw paragraph that contains all the recipe properties
    :return: list of individual recipe properties in a dictionary
    """
    recipes = {}
    pattern = r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (\d+)"
    for line in raw_input.split("\n"):
        m = match(pattern, line)
        recipes[m.group(1)] = {
            "capacity": int(m.group(2)),
            "durability": int(m.group(3)),
            "flavour": int(m.group(4)),
            "texture": int(m.group(5)),
            "calories": int(m.group(6))
        }
    return recipes


def calculate_score(recipes: dict, spoons: dict) -> int:
    capacity = durability = flavour = texture = 0
    for r in recipes:
        n = spoons[r] if spoons[r] else 0
        capacity += n * recipes[r]["capacity"]
        durability += n * recipes[r]["durability"]
        flavour += n * recipes[r]["flavour"]
        texture += n * recipes[r]["texture"]
    if capacity <= 0 or durability <= 0 or flavour <= 0 or texture <= 0:
        return 0
    else:
        return capacity * durability * flavour * texture


def calculate_calories(recipes: dict, spoons: dict) -> int:
    calories = 0
    for r in recipes:
        n = spoons[r] if spoons[r] else 0
        calories += n * recipes[r]["calories"]
    return calories


def highest_scoring_cookie(raw_input: str, calorie_restriction=False) -> int:
    recipes = parse_info(raw_input)
    recipe_names = [key for key in recipes.keys()]
    combinations = combinations_with_replacement(recipe_names, 100)
    max_score = float("-inf")
    for combination in combinations:
        spoons = Counter(combination)
        score = calculate_score(recipes, spoons)
        if not calorie_restriction or calculate_calories(recipes, spoons) == 500:
            max_score = max(max_score, score)
    return max_score


if __name__ == "__main__":
    input = read_file("inputs/input.txt")
    print(f"Total score of the highest-scoring cookie: {highest_scoring_cookie(input)}")
    print(f"Total score of the highest-scoring cookie with 500 calories: {highest_scoring_cookie(input, True)}")
