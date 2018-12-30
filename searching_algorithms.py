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

        while nodes_to_expand:
            if not nodes_to_expand:
                print("No result found!")
                return None
            current_state = nodes_to_expand.pop()
            number_of_expanded_nodes = number_of_expanded_nodes + 1
            if self.problem.isGoalTest(current_state):
                print("Algorithm: Graph DFS")
                print("Number Of Visited Nodes: " + str(number_of_visited_nodes))
                print("Number Of Expanded Nodes: " + str(number_of_expanded_nodes))
                print("Memory: " + str(self.memory))
                print("Last State: " + str(current_state))
                self.print_path(current_state)
                return current_state
            visited_nodes.append(current_state)
            states = self.problem.results(self.problem.actions(current_state), current_state)
            for state in states:
                if state not in visited_nodes:
                    number_of_visited_nodes = number_of_visited_nodes + 1
                    nodes_to_expand.append(state)
                    self.parent[state] = current_state
                    self.memory = self.memory + 1

    def tree_depth_first_search(self, start_state):
        path = []
        nodes_to_expand = [start_state]
        number_of_expanded_nodes = 0

        while nodes_to_expand:
            if not nodes_to_expand:
                print("No result found!")
                return None
            current_state = nodes_to_expand.pop()
            path.append(current_state)
            number_of_expanded_nodes = number_of_expanded_nodes + 1
            if self.problem.isGoalTest(current_state):
                print("Algorithm: Tree DFS")
                print("Number Of Expanded Nodes: " + str(number_of_expanded_nodes))
                print("Memory: " + str(self.memory))
                print("Last State: " + str(current_state))
                self.tree_print_path(path)
                return current_state
            states = self.problem.results(self.problem.actions(current_state), current_state)
            for state in states:
                nodes_to_expand.append(state)
                self.memory = self.memory + 1