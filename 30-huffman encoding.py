from collections import deque

import pdb


"""
              10     
           /      \
          /        \ 
         /          \
        3            7
      /    \       /   \
     /      \     /     \
    1B      2A   3C      4D
"""


class Node:
    def __init__(self, left, right, value, freq, height=0):
        self.right = right
        self.left = left
        self.letter = value
        self.freq = freq
        self.height = height

    def __str__(self) -> str:
        return f"Node({self.right==None},{self.left==None},{self.freq},{self.letter},{self.height})"


# step1
def make_freq(string: str):
    frequencies = sorted(
        [(s, string.count(s)) for s in dict.fromkeys(string)], key=lambda x: x[1]
    )
    return frequencies


# step 2
def create_huffman_tree(frequencies) -> Node:
    flag = 0
    queue = deque()
    queue2 = deque()
    queue += [
        Node(
            None,
            None,
            letters,
            length,
        )
        for letters, length in frequencies
    ]

    while len(queue) or len(queue2) > 1:
        min = 10000000
        if len(queue) > 1 and queue[0].freq + queue[1].freq < min:
            min = queue[0].freq + queue[1].freq
            flag = 0
        if len(queue) and len(queue2) and queue[0].freq + queue2[0].freq < min:
            min = queue[0].freq + queue2[0].freq
            flag = 1
        if len(queue2) > 1 and queue2[0].freq + queue2[1].freq < min:
            flag = 2

        match flag:
            case 0:
                left = queue.popleft()
                right = queue.popleft()

            case 1:
                left = queue2.popleft()
                right = queue.popleft()

            case 2:
                left = queue2.popleft()
                right = queue2.popleft()

        root_node = Node(
            left,
            right,
            left.letter + right.letter,
            left.freq + right.freq,
        )
        queue2.append(root_node)
    else:
        return root_node

def calculate_height_from_root(root_node):
    pass

# printing the huffman tree
def print_huffman_tree(root_node: Node):
    queue = deque()
    queue.append(root_node)

    current_index = 1
    current_capacity = 2

    while queue:
        node = queue.popleft()

        if node and node.left:
            queue.append(node.left)

        if node and node.right:
            queue.append(node.right)

        if current_index < current_capacity:
            print(f"{node.freq}{node.letter}", end="\t")
        else:
            print(f"\n{node.freq}{node.letter}", end="\t")
            current_capacity *= 2

        current_index += 1


# step 4
def encode(letter, node: Node, code=""):
    if node.letter == letter:
        return code
    elif node.left and (left_code := encode(letter, node.left, code + "0")):
        return left_code
    elif node.right and (right_code := encode(letter, node.right, code + "1")):
        return right_code
    else:
        return ""


string = "hello world"
frequencies = make_freq(string)

print(frequencies, end="\n\n")

root_node = create_huffman_tree(frequencies)

mapper = {l: encode(l, root_node) for l, f in frequencies}
print_huffman_tree(root_node)

print("\n\n\n" + str(mapper), end="\n\n\n")

for s in string:
    print(mapper[s], end=" ")
