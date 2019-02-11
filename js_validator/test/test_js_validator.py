from ..js_validator import is_valid_js


def test_is_valid_js():
    test_sequence1 = "{[]()}"
    test_sequence2 = "{ [ ( ] ) }"
    test_sequence3 = "{ [ }"

    assert is_valid_js(test_sequence1) is True
    assert is_valid_js(test_sequence2) is False
    assert is_valid_js(test_sequence3) is False