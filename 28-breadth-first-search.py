import pdb
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


breadth_first_search("you")


################## example 2
from os import listdir
from os.path import join, isfile


def iterate_folder(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)

    while search_queue:
        dir = search_queue.popleft()

        for path in sorted(listdir(dir)):
            full_path = join(dir, path)

            if "venv" in path or "git" in path:
                continue

            if isfile(full_path):
                print(f"file detected ==> {full_path}")
            else:
                search_queue.append(full_path)


iterate_folder("ex")
