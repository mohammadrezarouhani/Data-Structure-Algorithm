from collections import deque


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
    def __init__(self, left, right, value, factor, height):
        self.right = right
        self.left = left
        self.value = value
        self.factor = factor
        self.height = height

# step1
def make_factor(string: str):
    factors = sorted([(s, string.count(s)) for s in set(string)], key=lambda x: x[1])
    return factors

#step 2 
def create_huffman_tree(factors) -> Node:
    i = 0
    height = 1
    queue = deque()
    level_length = len(factors) / 2
    queue += [Node(None, None, letters, length, 0) for letters, length in factors]

    while len(queue) > 1:
        left = queue.popleft()
        right = queue.popleft()

        if not (i < level_length):
            level_length //= 2
            height += 1

        root_node = Node(left, right, "", left.factor + right.factor, height)
        queue.append(root_node)
        i += 1
    else:
        return root_node

# printing the huffman tree 
def print_huffman_tree(root_node: Node):
    queue = deque()
    queue.append(root_node)
    current_height = root_node.height

    while queue:
        node = queue.popleft()

        if node.left and node.right:
            queue.append(node.left)
            queue.append(node.right)

        # print
        if node.height == current_height:
            print(f"{node.factor}{node.value}", end="\t")
        else:
            print(end="\n")
            print(f"{node.factor}{node.value}", end="\t")
            current_height = node.height

# step 4
def encode(letter, node: Node, code=""):
    if node.value == letter:
        return code
    elif node.left and (left_code := encode(letter, node.left, code + "0")):
        return left_code
    elif node.right and (right_code := encode(letter, node.right, code + "1")):
        return right_code
    else:
        return ""


string = "hello world,"

factors = make_factor(string)
root_node = create_huffman_tree(factors)
mapper = {l: encode(l, root_node) for l, f in factors}


print(factors,end="\n\n")

print_huffman_tree(root_node)

print("\n\n\n" + str(mapper), end="\n\n\n")

for s in string:
    print(mapper[s], end=" ")
