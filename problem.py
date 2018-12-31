import graph as g
from SearchAlgorithms.informed_searching_algorithms import *
from SearchAlgorithms.uninformed_searching_algorithms import *


class Problem:

    def __init__(self):
        self.romania_map = g.Graph()
        self.romania_map.add_edge('Neamt', 'Iasi', 87)
        self.romania_map.add_edge('Iasi', 'Vasuli', 92)
        self.romania_map.add_edge('Vasuli', 'Urziceni', 142)
        self.romania_map.add_edge('Urziceni', 'Hirsova', 98)
        self.romania_map.add_edge('Urziceni', 'Bucharest', 85)
        self.romania_map.add_edge('Hirsova', 'Eforie', 86)
        self.romania_map.add_edge('Bucharest', 'Giurgiu', 90)
        self.romania_map.add_edge('Bucharest', 'Fagaras', 211)
        self.romania_map.add_edge('Bucharest', 'Pitesti', 101)
        self.romania_map.add_edge('Fagaras', 'Sibiu', 99)
        self.romania_map.add_edge('Pitesti', 'Craiova', 138)
        self.romania_map.add_edge('Pitesti', 'RimnicuVilcea', 97)
        self.romania_map.add_edge('Craiova', 'RimnicuVilcea', 146)
        self.romania_map.add_edge('RimnicuVilcea', 'Sibiu', 80)
        self.romania_map.add_edge('Dobreta', 'Craiova', 120)
        self.romania_map.add_edge('Dobreta', 'Mehadia', 75)
        self.romania_map.add_edge('Mehadia', 'Lugoj', 70)
        self.romania_map.add_edge('Lugoj', 'Timisoara', 111)
        self.romania_map.add_edge('Timisoara', 'Arad', 118)
        self.romania_map.add_edge('Arad', 'Sibiu', 140)
        self.romania_map.add_edge('Arad', 'Zerind', 75)
        self.romania_map.add_edge('Oradea', 'Zerind', 71)
        self.romania_map.add_edge('Oradea', 'Sibiu', 151)

        self.parent_path = {}

    def initial_state(self):
        return 'Arad'

    def goal(self):
        return 'Bucharest'

    def goal_test(self, state):
        return state == 'Bucharest'

    def actions(self, state):
        neighbors = []
        for s in self.romania_map.graph[state]:
            neighbors.append(f'go({s[0]})')
        return neighbors

    def results(self, state, action):
        self.parent_path[state] = action[3:-1]
        return  action[3:-1]

    def cost(self, state1, action, state2):
        cost_value = -1
        if action[3:-1] == state2:
            for s in self.romania_map.graph[state1]:
                if s[0] == state2:
                    cost_value = s[1]
        return cost_value

    def heuristic(self, state):
        if state in 'Arad':
            return 366
        if state in 'Bucharest':
            return 0
        if state in 'Craiova':
            return 160
        if state in 'Dobreta':
            return 242
        if state in 'Eforie':
            return 161
        if state in 'Fagaras':
            return 178
        if state in 'Giurgiu':
            return 77
        if state in 'Hirsova':
            return 151
        if state in 'Iasi':
            return 226
        if state in 'Lugoj':
            return 244
        if state in 'Mehadia':
            return 241
        if state in 'Neamt':
            return 234
        if state in 'Oradea':
            return 380
        if state in 'Pitesti':
            return 98
        if state in 'RimnicuVilcea':
            return 193
        if state in 'Sibiu':
            return 253
        if state in 'Timisoara':
            return 329
        if state in 'Urziceni':
            return 80
        if state in 'Vasuli':
            return 199
        if state in 'Zerind':
            return 374
        else:
            return 'Wrong Input!'

    def print_path(self, path, dfs_bfs=False):

        final_path = ''
        check = True
        for p in self.parent_path:
            if check:
                while p:
                    final_path += p
                    final_path += ' -> '
                    p = self.parent_path.get(p)
                check = False
        print(f'My Examined Path Is: {final_path[:-4]}')


        for current_state, next_state in zip(path, path[1:]):
            print(f'{current_state} -> {next_state} |')
            return

        if dfs_bfs:
            cost = list(zip(path, path[1:])).__len__()
            print(f'\nTotal Cost: {cost}')


p = Problem()
csa = ClassicSearchAlgorithm(p)
bcsa = BeyondClassicSearchAlgorithm(p)

csa.graph_depth_first_search(p.initial_state())