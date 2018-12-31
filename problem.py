import searching_algorithms
import graph as g
class Problem:

    def __init__(self):
        self.graph = g.Graph()
        self.graph.add_edge('Neamt', 'Iasi', 87)
        self.graph.add_edge('Iasi', 'Vasuli', 92)
        self.graph.add_edge('Vasuli', 'Urziceni', 142)
        self.graph.add_edge('Urziceni', 'Hirsova', 98)
        self.graph.add_edge('Urziceni', 'Bucharest', 85)
        self.graph.add_edge('Hirsova', 'Eforie', 86)
        self.graph.add_edge('Bucharest', 'Giurgiu', 90)
        self.graph.add_edge('Bucharest', 'Fagaras', 211)
        self.graph.add_edge('Bucharest', 'Pitesti', 101)
        self.graph.add_edge('Fagaras', 'Sibiu', 99)
        self.graph.add_edge('Pitesti', 'Craiova', 138)
        self.graph.add_edge('Pitesti', 'RimnicuVilcea', 97)
        self.graph.add_edge('Craiova', 'RimnicuVilcea', 146)
        self.graph.add_edge('RimnicuVilcea', 'Sibiu', 80)
        self.graph.add_edge('Dobreta', 'Craiova', 120)
        self.graph.add_edge('Dobreta', 'Mehadia', 75)
        self.graph.add_edge('Mehadia', 'Lugoj', 70)
        self.graph.add_edge('Lugoj', 'Timisoara', 111)
        self.graph.add_edge('Timisoara', 'Arad', 118)
        self.graph.add_edge('Arad', 'Sibiu', 140)
        self.graph.add_edge('Arad', 'Zerind', 75)
        self.graph.add_edge('Oradea', 'Zerind', 71)
        self.graph.add_edge('Oradea', 'Sibiu', 151)

    def initial_state(self):
        return 'Arad'

    # def states(self):
    #     return

    def goal(self):
        return 'Bucharest'

    def goal_test(self, state):
        return  state == 'Bucharest'

    def actions(self, state):
        return  # list

    def results(self, state, action):
        return  # state

    def cost(self, state1, action, state2):
        return  # int

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
        def find_direction(current_state, next_state):
            # todo: write what to print here
            return

        print("Path:", end=" ")
        for current_state, next_state in zip(path, path[1:]):
            find_direction(current_state, next_state)

        if dfs_bfs:
            cost = list(zip(path, path[1:])).__len__()
            print(f'\nTotal Cost: {cost}')
