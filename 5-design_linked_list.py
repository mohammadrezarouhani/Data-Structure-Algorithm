
import pdb


class Node:
    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next_obj = next


class MyLinkedList:
    def __init__(self):
        self.start: Node = None
        self.tail: Node = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        else:
            pointed_node = self.start
            for i in range(index):
                pointed_node = pointed_node.next_obj

            return pointed_node.value

    def addAtHead(self, val: int) -> None:
        self.start = Node(val, self.start)

        if self.length == 0:
            self.tail = self.start

        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if self.tail:
            self.tail.next_obj = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.start = new_node

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return None

        node = self.start

        if index == self.length and index != 0:
            new_node = Node(val, node.next_obj)
            self.tail.next_obj = new_node
            self.tail = new_node
        elif index == self.length and index == 0:
            new_node = Node(val)
            self.tail = new_node
            self.start = new_node
        elif index == 0:
            self.start = Node(val, self.start)
        else:
            for i in range(index-1):
                node = node.next_obj

            new_node = Node(val, node.next_obj)
            node.next_obj = new_node

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        node = self.start

        if index == self.length-1 and index == 0:
            for i in range(index-1):
                node = node.next_obj
            self.tail = node
            self.start = node
            node.next_obj=None
            self.length-=1

        elif index == self.length-1:
            for i in range(index-1):
                node = node.next_obj

            self.tail = node
            node.next_obj=None
            self.length -= 1

        elif index > 0 and index < self.length:

            for i in range(index-1):
                node = node.next_obj
            pointed_node = node.next_obj
            node.next_obj = pointed_node.next_obj
            del pointed_node
            self.length -= 1

        elif index == 0:
            self.start = self.start.next_obj
            del node
            self.length -= 1
        else:
            return

    def print_all(self):
        node = self.start
        li = []
        for i in range(self.length):

            li.append(node.value)
            node = node.next_obj

        return li


lni = MyLinkedList()
op=["MyLinkedList","addAtHead","addAtHead","deleteAtIndex"]

inputs=[[],[2],[1],[1]]

for index, operation in enumerate(op):
    inp = inputs[index]
    if op == 'MyLinkedList':
        lni = MyLinkedList()
    if operation == 'get':
        lni.get(inp[0])
    if operation == 'addAtHead':
        lni.addAtHead(inp[0])
    if operation == 'addAtTail':
        lni.addAtTail(inp[0])
    if operation == 'addAtIndex':
        lni.addAtIndex(inp[0], inp[1])
    if operation == 'deleteAtIndex':
        lni.deleteAtIndex(inp[0])
else:
    print(lni.print_all())
