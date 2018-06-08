from typing import Sequence

def jump_through_array(arr: Sequence)-> bool:
    current_location = 0
    end = len(arr) - 1

    while current_location < end:
        window_size: int = arr[current_location]

        if not window_size:
            return False

        window = arr[current_location + 1: current_location + 1 + window_size]

        # Tie breakers for two equal values says that values closer to
        # end are better ones to take. Enumerate starts at 1 and not 0 to
        # prevent the situation were 2 would be taken in the window [3, 2]
        window = [value + i for i, value in enumerate(window, 1)]

        current_location += window.index(max(window)) + 1 # because of 0 indexing

    return True