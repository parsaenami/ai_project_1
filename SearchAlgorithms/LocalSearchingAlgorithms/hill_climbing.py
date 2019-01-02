import random

class HillClimbing(object):

    def __init__(self, problem, type='greedy'):
        self.problem = problem
        self.type = type
        self.problem_solver(problem.initial_state())

    def problem_solver(self, initial_state):
        number_of_expanded_nodes = 0
        number_of_visited_nodes = 0
        best_state_found = False
        current_state = initial_state
        last_state = initial_state
        number_of_attempts = 5
        attempts = 0
        while not best_state_found:
            number_of_expanded_nodes = number_of_expanded_nodes + 1
            neighbors = self.problem.successor(current_state)
            number_of_visited_nodes = number_of_visited_nodes + len(neighbors)
            if self.type is 'greedy':
                current_state = self.find_neighbor_in_greedy_way(current_state, neighbors)
                best_state_found = True if last_state == current_state else False
            elif self.type is 'stochastic':
                current_state = self.find_neighbor_in_stochastic_way(current_state, neighbors)
                best_state_found = True if last_state == current_state else False
            elif self.type is 'random_restart':
                res = self.find_neighbor_in_random_restart_way(current_state, neighbors)
                current_state = res[0]
                number_of_visited_nodes += res[1]
                number_of_expanded_nodes += res[2]
                best_state_found = True if last_state == current_state else False
                # if last_state == current_state:
                #     if attempts < number_of_attempts:
                #         best_state_found = True
                #     attempts = attempts + 1
            elif self.type is 'first_choice':
                current_state = self.find_neighbor_in_first_choice_way(current_state, neighbors)
                best_state_found = True if last_state == current_state else False
            if self.problem.heuristic(current_state) == 0:
                best_state_found = True
            last_state = current_state
        print("Type of hill climbing: " + str(self.type))
        print("Number of colors: " + str(self.problem.color_size))
        print("Last state: " + str(current_state))
        print("Number of visited nodes: " + str(number_of_visited_nodes))
        print("Number of expanded nodes: " + str(number_of_expanded_nodes))
        temp = self.cost(current_state)
        print(f'Evaluation: {temp[1] - temp[0]} from {temp[1]} pair of nodes have different colors')

    def find_neighbor_in_greedy_way(self, current_state, neighbors):
        best_neighbor = current_state
        best_heuristic = self.problem.heuristic(current_state)
        for neighbor in neighbors:
            heuristic = self.problem.heuristic(neighbor)
            if heuristic < best_heuristic:
                best_heuristic = heuristic
                best_neighbor = neighbor
        return best_neighbor

    def find_neighbor_in_stochastic_way(self, current_state, neighbors):
        valuable_neighbors = []
        for neighbor in neighbors:
            if self.problem.heuristic(neighbor) < self.problem.heuristic(current_state):
                valuable_neighbors.append(neighbor)
        return random.choice(valuable_neighbors) if len(valuable_neighbors) > 0 else current_state

    def find_neighbor_in_first_choice_way(self, current_state, neighbors):
        best_heuristic = self.problem.heuristic(current_state)
        for neighbor in neighbors:
            heuristic = self.problem.heuristic(neighbor)
            if heuristic < best_heuristic:
                return neighbor
        return current_state

    def find_neighbor_in_random_restart_way(self, current_state, neighbors):
        best_answer = current_state
        best_state = False
        init_best_state = False
        init_best_state2 = False
        init_last_state = current_state
        answers = []
        visited, expanded = 0, 0
        # neighbors = self.problem.successor(current_state)

        while not init_best_state:
            state = self.find_neighbor_in_greedy_way(current_state, neighbors)
            init_best_state = True if state == init_last_state else False
            init_last_state = state
        answers.append(init_last_state)

        for i in range(300):
            current_state = self.problem.initial_state()
            expanded += 1
            neighbors = self.problem.successor(current_state)
            visited += len(neighbors)
            while not init_best_state2:
                state = self.find_neighbor_in_greedy_way(current_state, neighbors)
                init_best_state2 = True if state == init_last_state else False
                init_last_state = state
            answers.append(init_last_state)
            # print('************' + str(i))
            # print(answers.__len__())

        best_heuristic = self.problem.heuristic(current_state)
        for answer in answers:
            heuristic = self.problem.heuristic(answer)
            if heuristic < best_heuristic:
                best_heuristic = heuristic
                best_answer = answer

        return (best_answer, visited, expanded)

    def cost(self, current_state):
        same_color_edge = 0
        all_edge = 0
        graph = self.problem.cgraph.graph
        for g in graph:
            for n in graph[g]:
                all_edge += 1
                if current_state[n] == current_state[g]:
                    same_color_edge += 1

        return (same_color_edge // 2, all_edge // 2)