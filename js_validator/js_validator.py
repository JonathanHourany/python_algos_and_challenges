from typing import Iterable


def is_valid_js(js_code: Iterable) -> bool:
    openers_to_closers = {'(': ')',
                          '[': ']',
                          '{': '}'}
    openers = set(openers_to_closers.keys())
    closers = set(openers_to_closers.values())
    openers_stack = []

    for ch in js_code:
        if ch in openers:
            openers_stack.append(ch)
        elif ch in closers:
            if not openers_stack:
                return False
            current_opener = openers_stack.pop()
            if openers_to_closers[current_opener] != ch:
                return False

    return openers_stack == []
