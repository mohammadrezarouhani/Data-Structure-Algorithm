class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self, li=[]) -> None:
        self.top = None
        self.bottom = None

        for val in li:
            self.push(val)

    def push(self, value):
        self.bottom=self.top
        new_node = Node(value, self.top)
        self.top = new_node
        return True

    def pop(self):
        top = self.top
        self.top = self.top.next
        return top

    def print(self):
        pointer = self.top

        while pointer:
            print(pointer.value)
            pointer = pointer.next


s = Stack([1, 2, 3, 4, 5, 6, 7, 8, 9])

s.print()
