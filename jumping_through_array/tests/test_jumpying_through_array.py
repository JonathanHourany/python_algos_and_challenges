from ..jumping_through_array import jump_through_array

def test_jump_through_array():
    assert jump_through_array([3, 3, 1, 0, 2, 0, 0]) == True
    assert jump_through_array([3, 2, 0, 0, 4, 1, 1]) == False
    assert jump_through_array([5, 4, 3, 3, 2, 0, 1]) == True