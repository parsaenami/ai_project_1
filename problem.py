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


