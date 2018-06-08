from ..linked_list import SinglyLinkedList

def test_LinkedList():
    ll = SinglyLinkedList()
    assert len(ll) == 0

    ll.append(0)
    assert ll[0].obj == 0

    ll.append(1)
    assert ll[1].obj == 1

    node = ll.pop(1)
    assert node.obj == 1
    assert len(ll) == 1
