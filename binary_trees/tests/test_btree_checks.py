import pytest
from ..binary_tree_node import BinaryTreeNode
from ..btree_checks import is_superbalanced, is_valid

# Builds a balanced tree
btree_root = BinaryTreeNode(5)
btree_root.insert_right(2)
btree_root.insert_left(8)
btree_root.right.insert_right(1)
btree_root.right.insert_left(3)
btree_root.left.insert_right(7)
btree_root.left.insert_left(9)


def test_is_valid_true():
    assert is_valid(btree_root) is True


def test_is_balanced_true():
    assert is_superbalanced(btree_root) is True


def test_is_balanced_false():
    btree_root.right.right.insert_right(999)
    btree_root.right.right.right.insert_right(-999)
    assert is_superbalanced(btree_root) is False


def test_is_valid_false():
    assert is_valid(btree_root) is False
