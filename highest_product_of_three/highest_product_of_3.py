from typing import List

def highest_product_of_3(list_of_ints:List) -> int:
    if len(list_of_ints) < 3:
        raise ValueError('requires at least three elements')

    first_element, second_element, third_element = list_of_ints[0], list_of_ints[1], list_of_ints[2]
    highest_p_of_3 = first_element * second_element * third_element
    highest_p_of_2 = first_element * second_element
    highest_number = max(first_element, second_element)
    lowest_p_of_2 = first_element * second_element
    lowest_number = min(first_element, second_element)

    for i in list_of_ints[2:]:
        highest_p_of_3 = max(highest_p_of_3,
                             highest_p_of_2 * i,
                             lowest_p_of_2 * i)

        lowest_p_of_2 = min(lowest_p_of_2,
                            lowest_number * i)
        highest_p_of_2 = max(highest_p_of_2,
                             highest_number * i)

        highest_number = max(highest_number, i)
        lowest_number = min(lowest_number, i)

    return highest_p_of_3


def highest_product_of_3_alternative(list_of_ints):
    """A less ugly way of achieving the same results as highest_product_of_3 if you list isn't huge"""
    if len(list_of_ints) < 3:
        raise ValueError('requires at least three elements')

    sorted_list = sorted(list_of_ints)

    highest = max(sorted_list[-3] * sorted_list[-2] * sorted_list[-1],
                  sorted_list[0] * sorted_list[1] * sorted_list[-1])
    return highest