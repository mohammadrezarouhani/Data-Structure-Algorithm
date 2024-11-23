import math

# 1- start with lowest cost neighbor also check if node are processed or not
# 2- update its neighbor
# 3- repeat until there is unprocessed node


def find_smallest_cost_node(costs, processed):
    smallest = math.inf
    smallest_node = None

    for c in costs.keys():
        if costs[c] < smallest and not c in processed:
            smallest = costs[c]
            smallest_node = c

    return smallest_node


def dijkstra(graph, start_node: str, end_node: str):
    processed = []
    costs: dict = graph[start_node]
    costs.update({end_node: math.inf})

    parents = {key: start_node for key in graph[start_node]}
    parents.update({end_node: None})

    node = find_smallest_cost_node(costs, processed)

    while node:
        neighbors: dict = graph[node]
        for n in neighbors.keys():
            new_cost = neighbors[n] + costs[node]

            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        else:
            processed.append(node)
            node = find_smallest_cost_node(costs, processed)
    else:
        return costs, parents


if __name__ == "__main__":
    graph = {"Start": {"A": 6, "B": 2}, "A": {"Fin": 1}, "B": {"A": 3, "Fin": 4}, "Fin": {}}

    print(dijkstra(graph, "Start", "Fin"))
