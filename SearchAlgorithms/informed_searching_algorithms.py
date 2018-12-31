import sys



class BeyondClassicSearchAlgorithm(object):
    def __init__(self, problem):
        self.problem = problem
        self.parent = {}
        self.memory = 0

    def find_node_with_minimum_cost_to_expand(self, nodes):
        min_cost = sys.maxsize
        min_node = ()
        for node in nodes:
            if min_cost > node[1] + self.problem.heuristic(node[0]):
                min_cost = node[1]
                min_node = node
        return min_node

    def find_node_with_minimum_cost_to_expand_greedy(self, nodes):
        min_cost = sys.maxsize
        min_node = ()
        for node in nodes:
            if min_cost > self.problem.heuristic(node[0]):
                min_cost = self.problem.heuristic(node[0])
                min_node = node
        return min_node

    def graph_a_star(self, start_state):
        path_cost = 0
        visited_nodes = []
        number_of_visited_nodes = 1
        number_of_expanded_nodes = 0
        nodes_to_expand = [(start_state, path_cost)]

        while nodes_to_expand:
            if not nodes_to_expand:
                print("No result found!")
                return None
            current_state = self.find_node_with_minimum_cost_to_expand(nodes_to_expand)
            number_of_expanded_nodes = number_of_expanded_nodes + 1
            nodes_to_expand.pop(nodes_to_expand.index(current_state))
            path_cost = current_state[1]
            if self.problem.goal_test(current_state[0]):
                print("Algorithm: Graph A* Search")
                print("Number Of Visited Nodes: " + str(number_of_visited_nodes))
                print("Number Of Expanded Nodes: " + str(number_of_expanded_nodes))
                print("Cost: " + str(path_cost))
                print("Memory: " + str(self.memory))
                print("Last State: " + str(current_state))
                self.print_path(current_state[0])
                return current_state[0]
            visited_nodes.append(current_state[0])
            states = self.problem.results(self.problem.actions(current_state[0]), current_state[0])
            for state in states:
                if state not in visited_nodes:
                    number_of_visited_nodes = number_of_visited_nodes + 1
                    # nodes_to_expand.append((state, path_cost + self.problem.cost(current_state[0], self.problem.actions(current_state[0]), state) + self.problem.heuristic(state)))
                    nodes_to_expand.append((state, path_cost + self.problem.cost(current_state[0], self.problem.actions(current_state[0]), state)))
                    self.parent[state] = current_state[0]
                    self.memory = max(self.memory, len(nodes_to_expand))

    def tree_a_star(self, start_state):
        path = []
        path_cost = 0
        number_of_expanded_nodes = 0
        nodes_to_expand = [(start_state, path_cost)]

        while nodes_to_expand:
            if not nodes_to_expand:
                print("No result found!")
                return None
            current_state = self.find_node_with_minimum_cost_to_expand(nodes_to_expand)
            number_of_expanded_nodes = number_of_expanded_nodes + 1
            path.append(current_state[0])
            nodes_to_expand.pop(nodes_to_expand.index(current_state))
            path_cost = current_state[1]
            if self.problem.goal_test(current_state[0]):
                print("Algorithm: Tree A* Search")
                print("Number Of Expanded Nodes: " + str(number_of_expanded_nodes))
                print("Cost: " + str(path_cost))
                print("Memory: " + str(self.memory))
                print("Last State: " + str(current_state))
                self.tree_print_path(path)
                return current_state[0]
            states = self.problem.results(self.problem.actions(current_state[0]), current_state[0])
            for state in states:
                nodes_to_expand.append((state, path_cost + self.problem.cost(current_state[0], self.problem.actions(current_state[0]), state)))
                self.memory = max(self.memory, len(nodes_to_expand))

    def print_path(self, leaf_node):
        path = []
        while leaf_node:
            path.append(leaf_node)
            if leaf_node in self.parent:
                leaf_node = self.parent[leaf_node]
            else:
                leaf_node = None
        self.problem.print_path(list(reversed(path)))

    def tree_print_path(self, path):
        self.problem.print_path(list(path))
        # for item in path:
        #     print(item)

    def graph_greedy_best_first_search(self, start_state):
        path_cost = 0
        path = []
        visited_nodes = []
        number_of_visited_nodes = 1
        number_of_expanded_nodes = 0
        nodes_to_expand = [(start_state, path_cost)]

        while nodes_to_expand:
            if not nodes_to_expand:
                print("No result found!")
                return None
            current_state = self.find_node_with_minimum_cost_to_expand_greedy(nodes_to_expand)
            path.append(current_state[0])
            number_of_expanded_nodes = number_of_expanded_nodes + 1
            nodes_to_expand.pop(nodes_to_expand.index(current_state))
            path_cost = current_state[1]
            if self.problem.goal_test(current_state[0]):
                print("Algorithm: Graph GBFS")
                print("Number Of Visited Nodes: " + str(number_of_visited_nodes))
                print("Number Of Expanded Nodes: " + str(number_of_expanded_nodes))
                print("Cost: " + str(path_cost))
                print("Memory: " + str(self.memory))
                print("Last State: " + str(current_state))
                self.tree_print_path(path)
                # self.print_path(current_state[0])
                return current_state[0]
            visited_nodes.append(current_state[0])
            states = self.problem.results(self.problem.actions(current_state[0]), current_state[0])
            for state in states:
                if state not in visited_nodes:
                    number_of_visited_nodes = number_of_visited_nodes + 1
                    nodes_to_expand.append((state, path_cost + self.problem.cost(current_state[0], self.problem.actions(current_state[0]), state)))
                    self.parent[state] = current_state[0]
                    self.memory = max(self.memory, len(nodes_to_expand))

    def tree_greedy_best_first_search(self, start_state):
        # print("started")
        path = []
        path_cost = 0
        number_of_expanded_nodes = 0
        nodes_to_expand = [(start_state, path_cost)]

        cities = []
        costs = []

        while nodes_to_expand:
            if not nodes_to_expand:
                print("No result found!")
                return None
            current_state = self.find_node_with_minimum_cost_to_expand_greedy(nodes_to_expand)
            path.append(current_state[0])
            for i in nodes_to_expand:
                cities.append(i[0])
                costs.append(i[1])
            number_of_expanded_nodes = number_of_expanded_nodes + 1
            nodes_to_expand.pop(nodes_to_expand.index(current_state))
            path_cost = current_state[1]
            if self.problem.goal_test(current_state[0]):
                print("Algorithm: Tree GBFS")
                print("Number Of Expanded Nodes: " + str(number_of_expanded_nodes))
                print("Cost: " + str(path_cost))
                print("Memory: " + str(self.memory))
                print("Last State: " + str(current_state))
                self.tree_print_path(path)
                return current_state[0]
            states = self.problem.results(self.problem.actions(current_state[0]), current_state[0])
            for state in states:
                temp = (state, path_cost + self.problem.cost(current_state[0], self.problem.actions(current_state[0]), state))
                if temp[0] not in cities or (temp[0] in cities and temp[1] < costs[cities.index(temp[0])]):
                    nodes_to_expand.append(temp)
                if state in self.problem.results(self.problem.actions(current_state[0]), current_state[0]):
                    self.parent[state] = current_state[0]
                self.memory = max(self.memory, len(nodes_to_expand))
