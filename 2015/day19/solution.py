from re import match


def read_file(file_path: str) -> str:
    with open(file_path) as input_file:
        return input_file.read()


def parse_rules(raw_input: str) -> tuple[list[tuple], str]:
    pattern = r"(\w+) => (\w+)"
    lines = raw_input.split("\n")
    molecule = ""
    rules = []
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            molecule = line
        elif i != len(lines) - 2:
            m = match(pattern, line)
            rules.append((m.group(1), m.group(2)))
    return rules, molecule


def distinct_molecules(raw_input: str) -> int:
    rules, molecule = parse_rules(raw_input)
    molecules = set()
    for key, rule in rules:
        # search for all occurrences of the rule key in the string molecule and store the starting index if found
        indices = []
        start_index = 0
        while True:
            index = molecule.find(key, start_index)
            if index == -1:
                break  # not found
            else:
                indices.append(index)
                start_index = index + 1  # update starting index to continue searching until the end of the string
        for i in indices:
            molecules.add(molecule[:i] + rule + molecule[i + len(key):])
    return len(molecules)


def generate_molecule(raw_input: str) -> int:
    """
    Work backward from the target molecule to "e" using greedy reduction
    """
    rules, molecule = parse_rules(raw_input)

    # sort the rules from longest to shortest target string to run the largest reduction first
    rules.sort(key=lambda x: len(x[1]), reverse=True)

    # BFS queue starting with the target molecule
    queue = {molecule}
    visited = {molecule}

    steps = 0
    while True:
        steps += 1
        next_level_candidates = set()

        # generate all possible next states from the current set of strings through reduction
        for current_molecule in queue:
            # for each rule, find all occurrences of the substring and construct a new molecule
            for key, target in rules:
                # search for all occurrences of the target string in the molecule and store the starting index if found
                indices = []
                start_index = 0
                while True:
                    index = current_molecule.find(target, start_index)
                    if index == -1:
                        break  # not found
                    else:
                        indices.append(index)
                        start_index = index + 1  # continue searching until the end of the string
                for i in indices:
                    new_molecule = current_molecule[:i] + key + current_molecule[i + len(target):]
                    if new_molecule == "e":
                        return steps
                    if new_molecule not in visited:
                        next_level_candidates.add(new_molecule)

        # beam search with hardcoded width of 100 to reduce search space
        if len(next_level_candidates) > 100:
            sorted_candidates = sorted(list(next_level_candidates), key=len)
            queue = set(sorted_candidates[:100])
        else:
            queue = next_level_candidates

        if not queue:
            return -1  # not found

        visited.update(queue)


def cheat(raw_input: str) -> int:
    """
    This is not a general solution
    total steps = (total atoms) - (extra atoms from parentheses) - (extra atoms from commas) - 1
    """
    rules, molecule = parse_rules(raw_input)
    return sum(c.isupper() for c in molecule) - molecule.count("Rn") - molecule.count("Ar") - 2 * molecule.count("Y") - 1


if __name__ == "__main__":
    input = read_file("inputs/input.txt")
    print(f"Number of distinct molecules that can be created: {distinct_molecules(input)}")
    print(f"Fewest steps to go from 'e' to medicine molecule: {generate_molecule(input)}")
