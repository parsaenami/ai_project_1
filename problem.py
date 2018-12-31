class Problem:

    def initial_state(self):
        return

    # def states(self):
    #     return

    def goal(self):
        return

    def goal_test(self, state):
        return  # bool

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
