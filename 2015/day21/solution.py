import re
from itertools import combinations

item_shop = {
    "weapons": {
        "dagger": (8, 4, 0),  # cost, damage, armour
        "shortsword": (10, 5, 0),
        "warhammer": (25, 6, 0),
        "longsword": (40, 7, 0),
        "greataxe": (74, 8, 0)
    },
    "armour": {
        "leather": (13, 0, 1),
        "chainmail": (31, 0, 2),
        "splintmail": (53, 0, 3),
        "bandedmail": (75, 0, 4),
        "platemail": (102, 0, 5)
    },
    "rings": {
        "damage +1": (25, 1, 0),
        "damage +2": (50, 2, 0),
        "damage +3": (100, 3, 0),
        "defence +1": (20, 0, 1),
        "defence +2": (40, 0, 2),
        "defence +3": (80, 0, 3)
    }
}


def read_file(file_path: str) -> str:
    with open(file_path) as input_file:
        return input_file.read()


def parse_boss_stats(raw_input: str) -> tuple[int, int, int] | None:
    pattern = re.compile(
        r"^Hit Points: (\d+)\n"
        r"^Damage: (\d+)\n"
        r"^Armor: (\d+)$",
        re.MULTILINE
    )

    match = pattern.search(raw_input)
    if match:
        hit_points = int(match.group(1))
        damage = int(match.group(2))
        armour = int(match.group(3))
        return hit_points, damage, armour
    else:
        return None


def find_min_gold_required(raw_input: str, reverse=False) -> int:
    min_gold = float("-inf") if reverse else float("inf")

    # consider all possible way to buy items
    # must have exactly one weapon
    # optional one armour
    # 0~2 rings

    # generate all possible item combinations
    combos = []
    for weapon in item_shop["weapons"]:
        # case 1: no armour + 0 ring
        combos.append((weapon, [], []))

        # case 2: no armour + 1 ring
        for case in list(combinations(item_shop["rings"], 1)):
            combos.append((weapon, [], case))

        # case 3: no armour + 2 rings
        for case in list(combinations(item_shop["rings"], 2)):
            combos.append((weapon, [], case))

        for armour in item_shop["armour"]:
            # case 4: 1 armour + 0 ring
            combos.append((weapon, [armour], []))

            # case 5: 1 armour + 1 ring
            for case in list(combinations(item_shop["rings"], 1)):
                combos.append((weapon, [armour], case))

            # case 6: 1 armour + 2 rings
            for case in list(combinations(item_shop["rings"], 2)):
                combos.append((weapon, [armour], case))

    for combo in combos:
        # reset stats
        boss_hit_points, boss_damage, boss_armour = parse_boss_stats(raw_input)
        player_hit_points = 100
        player_damage = 0
        player_armour = 0
        gold = 0

        # weapon
        gold += item_shop["weapons"][combo[0]][0]
        player_damage += item_shop["weapons"][combo[0]][1]
        player_armour += item_shop["weapons"][combo[0]][2]

        for armour in combo[1]:
            gold += item_shop["armour"][armour][0]
            player_damage += item_shop["armour"][armour][1]
            player_armour += item_shop["armour"][armour][2]

        # rings
        for ring in combo[2]:
            gold += item_shop["rings"][ring][0]
            player_damage += item_shop["rings"][ring][1]
            player_armour += item_shop["rings"][ring][2]

        while boss_hit_points > 0 and player_hit_points > 0:
            # player deals damage
            damage = max((player_damage - boss_armour), 1)
            boss_hit_points -= damage
            # boss deals damage
            damage = max((boss_damage - player_armour), 1)
            player_hit_points -= damage

        if reverse:
            if boss_hit_points > 0:
                min_gold = max(min_gold, gold)
        else:
            if boss_hit_points <= 0:
                min_gold = min(min_gold, gold)

    return min_gold


if __name__ == "__main__":
    input = read_file("inputs/input.txt")
    print(f"What is the least amount of gold you can spend and still win the fight: {find_min_gold_required(input)}")
    print(f"What is the most amount of gold you can spend and still lose the fight: {find_min_gold_required(input, True)}")
