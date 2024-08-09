from collections import deque


graph = {}

graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


# a dummy function
def process(name):
    return name[-1] == "y"


def breadth_first_search(start):
    search_queue = deque()
    searched_target = []
    search_queue += graph[start]

    while search_queue:
        node = search_queue.popleft()

        if not node in searched_target:
            if process(node):
                return "target found " + node
            else:
                search_queue += graph[node]
                searched_target.append(node)
    return False


print(breadth_first_search("you"))
