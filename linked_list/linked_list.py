
class ListNode():

    def __init__(self, obj=None, next_node=None):
        self.obj = obj
        self.next = next_node

    def __repr__(self):
        return str(self.obj)


class SinglyLinkedList():

    def __init__(self, node: ListNode=None):
        self.head_node = node
        self._len = 0

        if node:
            self._len = 1

    def append(self, obj):
        if not self.head_node:
            self.head_node = ListNode(obj)
            self._len = 1
            return

        for node in self:
            if node.next is None:
                node.next = ListNode(obj)
                self._len += 1
                break

    def pop(self, position):
        it = iter(self)
        prev_node = next(it)

        if not self._valid_position(position):
            raise IndexError

        # If popping the head
        if position == 0:
            node = self.head_node
            self.head_node = self.head_node.next
            self._len -= 1
            return node

        for i, curr_node in enumerate(it, 1):
            if i == position:
                prev_node.next = curr_node.next
                self._len -= 1
                return curr_node

    def _valid_position(self, position):
        return position <= self._len - 1

    def __getitem__(self, position):
        if not self._valid_position(position):
            raise IndexError

        for i, node in enumerate(self):
            if i == position:
                return node

    def __iter__(self):
        node = self.head_node
        while node:
            yield node
            node = node.next

    def __len__(self):
        return self._len

    def __repr__(self):
        s = "[{elements}]"
        return s.format(elements=', '.join([str(node.obj) for node in self]))
