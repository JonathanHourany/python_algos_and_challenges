from typing import Iterable

def group_numbers(sequence: Iterable) -> tuple:
    # This way, we can accept generators as well
    sequence = iter(sequence)
    group = [next(sequence)]
    result = []

    for element in sequence:
        if element != group[0]:
            result.append(group)
            group = [element]
        else:
            group.append(element)

    if group:
        result.append(group)

    return tuple(result)


def build_sequence(groups: Iterable[Iterable]) -> str:
    result = ''
    for group in groups:
        # The repr builds strings from '111' to '31'
        group_repr = f"{len(group)}{group[0]}"
        result += group_repr
    return result


def look_and_say(n: int) -> tuple:
    results = ['1']

    for _ in range(1, n):
        groups = group_numbers(results[-1])
        next_sequence = build_sequence(groups)
        results.append(next_sequence)

    return tuple(results)


def main(num_iterations: int):
    results = look_and_say(num_iterations)
    print(results)

if __name__ == "__main__":
    main(6)