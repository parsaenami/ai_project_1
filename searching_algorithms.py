import sys


def find_node_with_minimum_cost_to_expand(nodes):
    min_cost = sys.maxsize
    min_node = ()
    for node in nodes:
        if min_cost > node[1]:
            min_cost = node[1]
            min_node = node
    return min_node


class ClassicSearchAlgorithm:

    def __init__(self, problem):
        self.problem = problem
        self.open_list = []
        self.close_list = []
        self.memory = 0
        self.parent = {}
        self.parent_from_goal = {}

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
        for item in path:
            print(item)

    def graph_depth_first_search(self, start_state):
        expanded_nodes_number, visited_nodes_number = 0, 1
        self.open_list.append(start_state)
        while self.open_list:
            current_state = self.open_list.pop(-1)
            expanded_nodes_number += 1
            self.close_list.append(current_state)
            if self.problem.goal_test(self.close_list[-1]):
                print('Algorithm: Tree Depth First Search')
                print(f'Number of Visited Nodes: {visited_nodes_number}')
                print(f'Number of Expanded Nodes: {expanded_nodes_number}')
                print(f'Maximum Memory: {self.memory}')
                print('The Best Route: ', end="")
                return
            states = self.problem.results(self.problem.actions(current_state), current_state)
            for state in states:
                if state not in self.close_list:
                    visited_nodes_number += visited_nodes_number
                    self.open_list.append(state)
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

    def graph_breadth_first_search(self, start_state):
        visited_nodes = []
        nodes_to_expand = [start_state]
        number_of_visited_nodes = 1
        number_of_expanded_nodes = 0

        while nodes_to_expand:
            if not nodes_to_expand:
                print("No result found!")
                return None
            current_state = nodes_to_expand.pop(0)
            number_of_expanded_nodes = number_of_expanded_nodes + 1
            if self.problem.isGoalTest(current_state):
                print("Algorithm: Graph BFS")
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

    def tree_breadth_first_search(self, start_state):
        path = []
        nodes_to_expand = [start_state]
        number_of_expanded_nodes = 0

        while nodes_to_expand:
            if not nodes_to_expand:
                print("No result found!")
                return None
            current_state = nodes_to_expand.pop(0)
            path.append(current_state)
            number_of_expanded_nodes = number_of_expanded_nodes + 1
            if self.problem.isGoalTest(current_state):
                print("Algorithm: Tree BFS")
                print("Number Of Expanded Nodes: " + str(number_of_expanded_nodes))
                print("Memory: " + str(self.memory))
                print("Last State: " + str(current_state))
                self.tree_print_path(path)
                return current_state
            states = self.problem.results(self.problem.actions(current_state), current_state)
            for state in states:
                nodes_to_expand.append(state)
                self.memory = self.memory + 1

    def graph_uniform_cost_search(self, start_state):
        path_cost = 0
        visited_nodes = []
        number_of_visited_nodes = 1
        number_of_expanded_nodes = 0
        nodes_to_expand = [(start_state, path_cost)]

        while nodes_to_expand:
            if not nodes_to_expand:
                print("No result found!")
                return None
            current_state = find_node_with_minimum_cost_to_expand(nodes_to_expand)
            number_of_expanded_nodes = number_of_expanded_nodes + 1
            nodes_to_expand.pop(nodes_to_expand.index(current_state))
            path_cost = current_state[1]
            if self.problem.isGoalTest(current_state[0]):
                print("Algorithm: Graph Uniform Cost Search")
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
                    nodes_to_expand.append((state, path_cost + self.problem.step_cost(current_state[0], state)))
                    self.parent[state] = current_state[0]
                    self.memory = self.memory + 1

    def tree_uniform_cost_search(self, start_state):
        path = []
        path_cost = 0
        number_of_expanded_nodes = 0
        nodes_to_expand = [(start_state, path_cost)]

        while nodes_to_expand:
            if not nodes_to_expand:
                print("No result found!")
                return None
            current_state = find_node_with_minimum_cost_to_expand(nodes_to_expand)
            path.append(current_state[0])
            number_of_expanded_nodes = number_of_expanded_nodes + 1
            nodes_to_expand.pop(nodes_to_expand.index(current_state))
            path_cost = current_state[1]
            if self.problem.isGoalTest(current_state[0]):
                print("Algorithm: Tree Uniform Cost Search")
                print("Number Of Expanded Nodes: " + str(number_of_expanded_nodes))
                print("Cost: " + str(path_cost))
                print("Memory: " + str(self.memory))
                print("Last State: " + str(current_state))
                self.tree_print_path(path)
                return current_state[0]
            states = self.problem.results(self.problem.actions(current_state[0]), current_state[0])
            for state in states:
                nodes_to_expand.append((state, path_cost + self.problem.step_cost(current_state[0], state)))
                self.parent[state] = current_state[0]
                self.memory = self.memory + 1

    def graph_depth_limited_search(self, start_state, depth):
        current_depth = 0
        visited_nodes = []
        nodes_to_expand = [(start_state, 0)]
        number_of_visited_nodes = 1
        number_of_expanded_nodes = 0

        while nodes_to_expand and current_depth <= depth:
            if not nodes_to_expand:
                print("No result found!")
                return None
            current_state = nodes_to_expand.pop()
            number_of_expanded_nodes = number_of_expanded_nodes + 1
            if self.problem.isGoalTest(current_state):
                print("Algorithm: Graph Depth Limited Search")
                print("Number Of Visited Nodes: " + str(number_of_visited_nodes))
                print("Number Of Expanded Nodes: " + str(number_of_expanded_nodes))
                print("Depth: " + str(current_depth))
                print("Memory: " + str(self.memory))
                print("Last State: " + str(current_state))
                print("Solution found in Depth " + str(current_depth))
                self.print_path(current_state)
                return current_state
            visited_nodes.append(current_state[0])
            states = self.problem.results(self.problem.actions(current_state[0]), current_state[0])
            current_depth = current_depth + 1
            for state in states:
                if state not in visited_nodes:
                    number_of_visited_nodes = number_of_visited_nodes + 1
                    nodes_to_expand.append(state)
                    self.parent[state] = current_state
                    self.memory = self.memory + 1

        print("No result found in depth " + str(depth))
        return None

    def tree_depth_limited_search(self, start_state, depth):
        path = []
        current_depth = 0
        nodes_to_expand = [(start_state, 0)]
        number_of_expanded_nodes = 0

        while nodes_to_expand and current_depth <= depth:
            if not nodes_to_expand:
                print("No result found!")
                return None
            current_state = nodes_to_expand.pop()
            path.append(current_state)
            number_of_expanded_nodes = number_of_expanded_nodes + 1
            if self.problem.isGoalTest(current_state):
                print("Algorithm: Tree Depth Limited Search")
                print("Number Of Expanded Nodes: " + str(number_of_expanded_nodes))
                print("Depth: " + str(current_depth))
                print("Memory: " + str(self.memory))
                print("Last State: " + str(current_state))
                print("Solution found in Depth " + str(current_depth))
                self.tree_print_path(path)
                return current_state
            states = self.problem.results(self.problem.actions(current_state[0]), current_state[0])
            current_depth = current_depth + 1
            for state in states:
                nodes_to_expand.append(state)
                self.parent[state] = current_state
                self.memory = self.memory + 1

        print("No result found in depth " + str(depth))
        return None

    def graph_iterative_deepening_search(self, start_state, depth=0):
        path = None
        while path is None:
            path = self.graph_depth_limited_search(start_state, depth)
            depth = depth + 1

    def tree_iterative_deepening_search(self, start_state, depth=0):
        path = None
        while path is None:
            path = self.tree_depth_limited_search(start_state, depth)
            depth = depth + 1