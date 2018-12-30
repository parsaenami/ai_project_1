class ClassicSearchAlgorithm(object):

    def __init__(self, problem):
        self.problem = problem
        self.parent = {}
        self.parent_from_goal = {}
        self.memory = 0

    def graph_depth_first_search(self, start_state):
        visited_nodes = []
        nodes_to_expand = [start_state]
        number_of_visited_nodes = 1
        number_of_expanded_nodes = 0