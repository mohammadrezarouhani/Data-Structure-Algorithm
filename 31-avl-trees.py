# creating a avl tree base on list of elements
from collections import deque
from typing import Deque, List


class AvlNode:
    def __init__(self, value, right=None, left=None, weight=0, height=0) -> None:
        self.value = value
        self.right = right
        self.left = left
        self.balance_factor = weight
        self.height = height

    def __repr__(self) -> str:
        repr = f"({self.value}"

        if self.right:
            repr += f",right({self.right.value})"

        if self.left:
            repr += f",left({self.left.value}))"

        return repr + ")"


def update_balance_factor(node: AvlNode):
    if node.left:
        left_height = update_balance_factor(node.left)
    else:
        left_height = node.height

    if node.right:
        right_height = update_balance_factor(node.right)
    else:
        right_height = node.height

    if node.left == None and node.right == None:
        node.balance_factor = 0
        return node.height
    else:
        node.balance_factor = left_height - right_height
        return max(left_height, right_height)


def check_balance(direction_queue: List[AvlNode]):
    for node in direction_queue:
        update_balance_factor(node)
        
    reversed = direction_queue[::-1]
    for index, node in enumerate(reversed):
        if node.balance_factor > 1 or node.balance_factor < -1:
            break
    else:
        return None

    direction = ""
    prev_node = None
    for node in reversed[: index + 1]:
        if prev_node and prev_node == node.left:
            direction += "L"
        elif prev_node and prev_node == node.right:
            direction += "R"

        prev_node = node

    return "".join(list(dict.fromkeys(direction[::-1]))), index


def rotate_tree(direction_queue):
    pass


def print_tree(root_node):
    queue = deque()
    queue.append(root_node)
    current_height = 0

    while queue:
        node = queue.popleft()

        if node.height != current_height:
            print(end="\n")
            current_height = node.height

        print(node.value, root_node.balance_factor, end="\t")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


def insert_into_avl_tree(new_node_value, root_node):
    direction = []

    if root_node == None:
        return AvlNode(new_node_value)
    else:
        pointer = root_node
        new_node = AvlNode(new_node_value)

    while True:
        direction.append(pointer)

        if new_node.value < pointer.value:
            if pointer.left != None:
                pointer = pointer.left
            else:
                new_node.height = pointer.height + 1
                pointer.left = new_node
                break
        else:
            if pointer.right != None:
                pointer = pointer.right
            else:
                new_node.height = pointer.height + 1
                pointer.right = new_node
                break

    direction.append(new_node)
    rotate_type, = check_balance(direction)

    if rotate_type:
        rotate_tree(rotate_type)

    return root_node


root_node = None
for node in [20, 15, 30, 25, 40, 35, 50, 45, 60]:
    root_node = insert_into_avl_tree(node, root_node)


print_tree(root_node)
