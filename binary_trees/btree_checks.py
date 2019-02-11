from .binary_tree_node import BinaryTreeNode
from typing import Union


# def is_superbalanced(node: BinaryTreeNode) -> Union[bool, int]:
#     if not node:
#         return 1
#
#     if not node.left and not node.right:
#         return 1
#     left_return = is_superbalanced(node.left)
#     right_return = is_superbalanced(node.right)
#     return left_return is right_return or left_return - right_return in (-1, 0, 1)


def is_superbalanced(node: BinaryTreeNode) -> Union[bool, int]:
    def helper(node) -> int:
        if not node:
            return 0

        left_return = helper(node.left)
        right_return = helper(node.right)
        print(f"self:{node.value}, right:{right_return}, left:{left_return}, total:{abs(left_return - right_return) + 1}")
        return abs(left_return - right_return) + 1

    return helper(node) in (0, 1)


def is_valid(node: BinaryTreeNode) -> bool:
    right_side = False
    left_side = False
    if not node:
        return True

    if not node.right or node.right.value < node.value:
        right_side = True

    if not node.left or node.left.value > node.value:
        left_side = True

    return right_side is left_side and is_valid(node.right) is is_valid(node.left)


def breadth_first_search(root_node: BinaryTreeNode, value) -> Union[BinaryTreeNode, None]:
    #retrived_node = None
    nodes = [root_node]

    while nodes:
        node = nodes.pop(0)
        if node:
            if node.value == value:
                return node

            nodes.extend([node.right, node.left])
    return None


def second_largest_in_tree(root_node: BinaryTreeNode) -> int:
    nodes = [root_node]
    max_so_far = [float('-inf'), float('-inf')]

    for node in nodes:
        if not node:
            continue

        nodes.extend([node.right, node.left])
        if node.value > max_so_far[-1]:
            max_so_far.pop(0)
            max_so_far.append(node.value)

    return max_so_far[0]