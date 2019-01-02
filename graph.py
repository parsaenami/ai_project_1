from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, node1, node2, cost):
        self.graph[node1].append([node2, cost])
        self.graph[node2].append([node1, cost])

    def add_edge_colored(self, node1, node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)