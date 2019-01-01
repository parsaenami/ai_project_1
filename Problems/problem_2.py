import random
from collections import defaultdict

import graph as g
from copy import deepcopy
from SearchAlgorithms.LocalSearchingAlgorithms.hill_climbing import *
from SearchAlgorithms.LocalSearchingAlgorithms.simulated_annealing import *
from SearchAlgorithms.LocalSearchingAlgorithms.genetic import *


# graph = {
#     1: [2, 3, 4, 5, 6],
#     2: [1, 7, 8],
#     3: [1, 8, 9],
#     4: [1, 9, 10],
#     5: [1, 10, 11],
#     6: [1, 7, 11],
#     7: [2, 6, 9, 10],
#     8: [2, 3, 10, 11],
#     9: [3, 4, 7, 11],
#     10: [4, 5, 7, 8],
#     11: [5, 6, 8, 9]
# }


class Problem:

    def __init__(self, color_size):
        self.cgraph = g.Graph()
        self.color_size = color_size
        # self.initial_state()

    def initial_state(self):
        # self.cgraph = g.Graph()
        self.cgraph.graph.clear()
        self.cgraph.add_edge_colored(1, 2)
        self.cgraph.add_edge_colored(1, 3)
        self.cgraph.add_edge_colored(1, 4)
        self.cgraph.add_edge_colored(1, 5)
        self.cgraph.add_edge_colored(1, 6)
        self.cgraph.add_edge_colored(2, 7)
        self.cgraph.add_edge_colored(2, 8)
        self.cgraph.add_edge_colored(3, 8)
        self.cgraph.add_edge_colored(3, 9)
        self.cgraph.add_edge_colored(4, 9)
        self.cgraph.add_edge_colored(4, 10)
        self.cgraph.add_edge_colored(5, 10)
        self.cgraph.add_edge_colored(5, 11)
        self.cgraph.add_edge_colored(6, 7)
        self.cgraph.add_edge_colored(6, 11)
        self.cgraph.add_edge_colored(7, 9)
        self.cgraph.add_edge_colored(7, 10)
        self.cgraph.add_edge_colored(8, 10)
        self.cgraph.add_edge_colored(8, 11)
        self.cgraph.add_edge_colored(9, 11)

        # self.states = {}
        return self.new_state()

    def new_state(self):
        node_colors = defaultdict(list)
        for g in self.cgraph.graph:
            node_colors[g] = random.randrange(self.color_size)
        return node_colors

    def successor(self, current_state):
        all_neighbors = self.find_all_neighbors()
        num_of_neighbors = {}
        neighbors = []
        for i in current_state:
            num_of_neighbors[i] = 0
        for neighbor in all_neighbors:
            if current_state[neighbor[0]] == current_state[neighbor[1]]:
                num_of_neighbors[neighbor[0]] = num_of_neighbors[neighbor[0]] + 1
                num_of_neighbors[neighbor[1]] = num_of_neighbors[neighbor[1]] + 1
        worst_node = max(num_of_neighbors, key=num_of_neighbors.get)
        for i in range(self.color_size):  # colors
            temp_state = deepcopy(current_state)
            if temp_state[worst_node] != i:
                temp_state[worst_node] = i
                neighbors.append(temp_state)
        return neighbors

    def find_all_neighbors(self):
        all_neighbors = []
        for i in self.cgraph.graph:
            for j in self.cgraph.graph[i]:
                all_neighbors.append((i, j))
        return all_neighbors

    def heuristic(self, node_colors):
        score = 0
        all_neighbors = self.find_all_neighbors()
        for i in all_neighbors:
            if node_colors[i[0]] == node_colors[i[1]]:
                score = score + 1
        return score

p = Problem(3)
print('-----------------------------------------------------------------------')
print('                           HILL CLIMBING')
print('-----------------------------------------------------------------------')
hc1 = HillClimbing(p, 'first_choice')
print('-----------------------------------------------------------------------')
hc2 = HillClimbing(p, 'stochastic')
print('-----------------------------------------------------------------------')
hc3 = HillClimbing(p, 'random_restart')
print('-----------------------------------------------------------------------')
hc4 = HillClimbing(p, 'greedy')
print('-----------------------------------------------------------------------')
print('                        simulated annealing'.upper())
print('-----------------------------------------------------------------------')
sa = SimulatedAnnealing(p)
print('-----------------------------------------------------------------------')
print('                              genetic'.upper())
print('-----------------------------------------------------------------------')
ge = Genetic(p, 50, 10, 2, 0.01)
print('-----------------------------------------------------------------------')
