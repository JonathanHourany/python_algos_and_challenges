from ..look_and_say import look_and_say

def test_look_and_say():
    assert look_and_say(5) == ('1', '11', '21', '1211', '111221')