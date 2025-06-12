from re import match


def read_file(file_path: str) -> str:
    with open(file_path) as input_file:
        return input_file.read()


def parse_replacements(raw_input: str) -> tuple[list[tuple], str]:
    pattern = r"(\w+) => (\w+)"
    lines = raw_input.split("\n")
    molecule = ""
    transitions = []
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            molecule = line
        elif i != len(lines) - 2:
            m = match(pattern, line)
            transitions.append((m.group(1), m.group(2)))
    return transitions, molecule


def distinct_molecules(raw_input: str) -> int:
    transitions, molecule = parse_replacements(raw_input)
    molecules = set()
    for key, transition in transitions:
        # search for all occurrences of the transition key in the string molecule and store the starting index if found
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
            molecules.add(molecule[:i] + transition + molecule[i + len(key):])
    return len(molecules)


def generate_molecule(raw_input: str) -> int:
    return 0


if __name__ == "__main__":
    input = read_file("inputs/input.txt")
    print(f"Number of distinct molecules that can be created: {distinct_molecules(input)}")
    print(f"Fewest steps to go from 'e' to medicine molecule: {generate_molecule(input)}")
