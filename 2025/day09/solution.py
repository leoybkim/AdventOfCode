from utils.input_reader import read_file


def parse_data(data: str) -> list:
    points = []
    for line in data.splitlines():
        points.append(tuple(map(int, line.split(","))))
    return points


def area(a: tuple, b: tuple) -> int:
    return (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)


def part_one(data: str):
    points = parse_data(data)  # tuple(column, row) of red carpet locations
    max_area = float('-inf')

    n = len(points)
    for i in range(n - 1):
        for j in range(i + 1, n):
            max_area = max(max_area, area(points[i], points[j]))

    return max_area


def in_boundary(segments: list[tuple[tuple[int, int], tuple[int, int]]],
                a: tuple[int, int],
                b: tuple[int, int]) -> bool:
    """
    Check if the rectangle formed by point a and b lies inside the polygon defined by segments.
    Iterating through all points in the rectangle formed by points a and b will cause performance issues.
    For complete testing, all 4 vertices must be inside (or on) the polygon as well as not have any polygon segments intersect the rectangle.
    Intersection check by itself cannot distinguish between the rectangle being completely outside the boundary vs completely inside the boundary.
    However, for the sake of this puzzle input, we already know that 2 of the 4 vertices that build the rectangle are already on the boundary segments.
    So we can skip the check on whether all vertices are inside the boundary because it will never be completely outside/
    """

    r_lo, r_hi = sorted((a[1], b[1]))
    c_lo, c_hi = sorted((a[0], b[0]))

    # Check if the rectangle formed by point a and b intersects any edges of the polygon boundary.
    # Touching at boundary lines is allowed, so we use strict inequalities.
    for (c1, r1), (c2, r2) in segments:
        if c1 == c2:
            # Vertical edge
            if c_lo < c1 < c_hi and not (max(r1, r2) <= r_lo or r_hi <= min(r1, r2)):
                return False
        elif r1 == r2:
            # Horizontal edge
            if r_lo < r1 < r_hi and not (max(c1, c2) <= c_lo or c_hi <= min(c1, c2)):
                return False
        else:
            # Should never enter here with the given input, all segments are either a horizontal or vertical edge
            continue
    return True


def part_two(data: str) -> int:
    points = parse_data(data)  # tuple(column, row) of red carpet locations
    max_area = float('-inf')
    n = len(points)

    # Build boundary as a list of segments instead of rasterizing a grid to be memory efficient
    segments: list[tuple[tuple[int, int], tuple[int, int]]] = []
    start_p = points[0]
    for i in range(1, n):
        next_p = points[i]
        segments.append((start_p, next_p))
        start_p = next_p
    # Complete the loop
    segments.append((points[-1], points[0]))

    # Loop through rectangles and see if it fits in the boundary, keep the largest area
    for i in range(n - 1):
        for j in range(i + 1, n):
            if in_boundary(segments, points[i], points[j]):
                max_area = max(max_area, area(points[i], points[j]))

    return max_area


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Largest area of the rectangle: {part_one(file)}")
    print(f"Largest area of the rectangle using only red and green tiles: {part_two(file)}")
