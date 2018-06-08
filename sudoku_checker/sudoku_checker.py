from typing import Iterable, List, Sequence

def get_rows(puzzle: Sequence[Sequence]) -> List:
    return [row for row in puzzle]


def get_columns(puzzle: Sequence[Sequence]) -> List:
    return [[row[i] for row in get_rows(puzzle)] for i in range(len(puzzle))]


def get_regions(puzzle: Sequence[Sequence]) -> List:
    regions = []

    # Traverse rows in sets of 3
    for i in range(0, 9, 3):
        rows = [puzzle[row_number] for row_number in range(i, i+3)]

        # Slide down columns in jumps of 3
        for j in range(0, 9, 3):
            region = [element for row in rows for element in row[j:j+3]]
            regions.append(region)
    return regions


def valid_sequence(sequence: Sequence[Sequence]) -> bool:
    for arr in sequence:
        # Check that all digits are in range(1,9)
        numbers = [number for number in arr if (0 < number < 10)]
        # Dedup any numbers
        numbers = set(numbers)
        if len(numbers) != len(arr):
            return False

    return True


def main(puzzle):
    rows = get_rows(puzzle)
    columns = get_columns(puzzle)
    regions = get_regions(puzzle)

    return all(valid_sequence(arr) for arr in (rows, columns, regions))

if __name__ == '__main__':
    puzzle = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
              [6, 7, 2, 1, 9, 5, 3, 4, 8],
              [1, 9, 8, 3, 4, 2, 5, 6, 7],
              [8, 5, 9, 7, 6, 1, 4, 2, 3],
              [4, 2, 6, 8, 5, 3, 7, 9, 1],
              [7, 1, 3, 9, 2, 4, 8, 5, 6],
              [9, 6, 1, 5, 3, 7, 2, 8, 4],
              [2, 8, 7, 4, 1, 9, 6, 3, 5],
              [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    main(puzzle)