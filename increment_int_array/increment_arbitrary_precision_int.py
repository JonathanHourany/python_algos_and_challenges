from typing import List, Tuple

def carry_over_addr(digit:int, carry_over:int)-> Tuple[int, int]:
    n = digit + carry_over
    carry_over = 0

    while not n < 10:
        carry_over +=1
        n -= 10

    return n, carry_over

def add_n(precision_array: List[int], n: int) -> List:
    reversed_precision_array = precision_array[::-1]
    addition_results = []
    carry_over = n

    for i, digit in enumerate(reversed_precision_array):
        result, carry_over = carry_over_addr(digit, carry_over)
        addition_results.append(result)
        if not carry_over:
            break

    addition_results += reversed_precision_array[i+1:]
    return addition_results[::-1]
