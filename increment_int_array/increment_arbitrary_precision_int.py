from typing import List, Tuple


def carry_over_addr(digit:int, carry_over:int)-> Tuple[int, int]:
    n = digit + carry_over
    remainder = 0
    if n < 10:
        return n, remainder

    integer, remainder = n%10, n//10

    return integer, remainder

def add_n(precision_array: List[int], n: int) -> List:
    if len(precision_array) < 1:
        raise ValueError(f"precision_array must contain at least one element, got {len(precision_array)}")

    reversed_precision_array = precision_array[::-1]
    addition_results = []
    carry_over = n

    for i, digit in enumerate(reversed_precision_array):
        result, carry_over = carry_over_addr(digit, carry_over)
        addition_results.append(result)
        # If there's nothing left to add, we can stop
        if not carry_over:
            break

    # If we broke early, this lets us simply copy was was remaining into our
    # array with the addition solved, instead of forcing us to iterate through a list of unknown size
    # making function calls we know won't do anything
    addition_results += reversed_precision_array[i+1:]
    return addition_results[::-1]
