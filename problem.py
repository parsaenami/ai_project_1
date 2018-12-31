class Problem:

    def initial_state(self):
        return

    # def states(self):
    #     return

    # def goal(self):
    #     return

    def goal_test(self, state):
        return  # bool

    def actions(self, state):
        return  # list

    def results(self, state, action):
        return  # state

    def cost(self, state1, action, state2):
        return  # int

    def heuristic(self, state):
        return  # int

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
