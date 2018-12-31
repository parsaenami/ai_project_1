from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = []
        self.edges = []

    def add_edge(self, node1, node2, cost):
        self.graph[node1].append((node2, cost))
        self.graph[node2].append((node1, cost))


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

    def print_path_from_goal(self, leaf_node):
        print("From goal", end=" ")
        path = []
        while leaf_node:
            path.append(leaf_node)
            if leaf_node in self.parent_from_goal:
                leaf_node = self.parent_from_goal[leaf_node]
            else:
                leaf_node = None
        self.problem.print_path(list(reversed(path)))

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

