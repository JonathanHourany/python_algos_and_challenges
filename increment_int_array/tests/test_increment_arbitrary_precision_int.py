from ..increment_arbitrary_precision_int import add_n

def test_increment_int_array():
    assert add_n([1, 2, 9], 5) == [1, 3, 4]
    assert add_n([1, 2, 9], 20) == [1, 4, 9]
    assert add_n([9, 9, 9], 1) == [0, 0, 0]
    assert add_n([9, 9, 9], 4) == [0, 0, 3]