import random
import math


class SimulatedAnnealing(object):

    def __init__(self, problem):
        self.problem = problem
        self.problem_solver(problem.initial_state())

    def problem_solver(self, initial_state):
        number_of_expanded_nodes = 0
        number_of_visited_nodes = 0
        current_state = initial_state
        initial_temperature = 10000
        current_temperature = initial_temperature
        while current_temperature > 1:
            number_of_expanded_nodes = number_of_expanded_nodes + 1
            neighbors = self.problem.successor(current_state)
            number_of_visited_nodes = number_of_visited_nodes + len(neighbors)
            chosen_neighbor = random.choice(neighbors)
            efficiency = self.problem.heuristic(chosen_neighbor) - self.problem.heuristic(current_state)
            if efficiency >= 0:
                current_state = chosen_neighbor
            else:
                if math.exp(efficiency / current_temperature) > random.random():
                    current_state = chosen_neighbor
            # 1
            current_temperature = current_temperature - 1
            # 2
            # current_temperature = current_temperature * 0.99
            # 3
            # current_temperature = math.sqrt(current_temperature)

        print("Number of colors: " + str(self.problem.color_size))
        print("Initial temperature: " + str(initial_temperature))
        print("Current temperature: " + str(current_temperature))
        print("Last state: " + str(current_state))
        print("Number of visited nodes: " + str(number_of_visited_nodes))
        print("Number of expanded nodes: " + str(number_of_expanded_nodes))
        temp = self.cost(current_state)
        print(f'Evaluation: {temp[1] - temp[0]} from {temp[1]} pair of nodes have different colors')

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
