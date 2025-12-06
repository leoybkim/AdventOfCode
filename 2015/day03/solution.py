from utils.input_reader import read_file


def count_houses(raw_input: str, robo=False) -> int:
    x = y = 0  # Initial starting location
    directions = {"<": (-1, 0), ">": (1, 0), "^": (0, 1), "v": (0, -1)}
    visited = {(x, y)}  # Create a set with initial position as the first value

    if robo:
        rx = ry = 0  # Robot santa starting location
        for i, c in enumerate(raw_input):
            dx, dy = directions[c]
            if i % 2 == 0:
                nx, ny = x + dx, y + dy
                visited.add((nx, ny))
                x, y = nx, ny  # Update Santa's current coordinate
            else:
                nx, ny = rx + dx, ry + dy
                visited.add((nx, ny))
                rx, ry = nx, ny  # Update Robo-Santa's current coordinate
    else:
        for c in raw_input:
            dx, dy = directions[c]
            nx, ny = x + dx, y + dy
            visited.add((nx, ny))
            x, y = nx, ny  # Update Santa's current coordinate

    return len(visited)


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Number of houses that receive at least one present: {count_houses(file)}")
    print(f"Number of houses that receive at least one present with Robo-Santa: {count_houses(file, robo=True)}")
