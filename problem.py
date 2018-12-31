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

    def results(self, action, state):
        actions = []
        for a in action:
            self.parent_path[state] = a[3:-1]
            actions.append(a[3:-1])

        return actions

    def cost(self, state1, action, state2):
        cost_value = -1
        if f'go({state2})' in action:
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

        # final_path = ''
        # check = True
        # for p in self.parent_path:
        #     if check:
        #         while p:
        #             final_path += p
        #             final_path += ' -> '
        #             p = self.parent_path.get(p)
        #         check = False
        # print(f'My Examined Path Is: {final_path[:-4]}')

        if dfs_bfs:
            cost = list(zip(path, path[1:])).__len__()
            print(f'Total Cost: {cost}')

        print('The Best Route: ', end="")
        temp = ''
        for current_state, next_state in zip(path, path[1:]):
            temp = next_state
            print(f'{current_state} -> ', end="")
        print(temp)
        return


p = Problem()
csa = ClassicSearchAlgorithm(p)
bcsa = BeyondClassicSearchAlgorithm(p)

# bcsa.graph_a_star(p.initial_state())
# bcsa.tree_a_star(p.initial_state())
bcsa.tree_greedy_best_first_search(p.initial_state())
print('-----------------------------------------------------------')
bcsa.graph_greedy_best_first_search(p.initial_state())

# csa.graph_depth_first_search(p.initial_state())               #ok
# csa.tree_depth_first_search(p.initial_state())                #ok...
# csa.graph_breadth_first_search(p.initial_state())             #ok
# csa.tree_breadth_first_search(p.initial_state())              #meh
# csa.graph_uniform_cost_search(p.initial_state())              #ok
# csa.tree_uniform_cost_search(p.initial_state())               #meh
# csa.graph_depth_limited_search(p.initial_state(), 3)          #ok
# csa.tree_depth_limited_search(p.initial_state(), 5)           #ok
# csa.graph_iterative_deepening_search(p.initial_state(), 3)    #ok
# csa.tree_iterative_deepening_search(p.initial_state(), 2)     #ok
