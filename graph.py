from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = []
        self.edges = []

    def add_edge(self, node1, node2, cost):
        self.graph[node1].append([node2, cost])
        self.graph[node2].append([node1, cost])
