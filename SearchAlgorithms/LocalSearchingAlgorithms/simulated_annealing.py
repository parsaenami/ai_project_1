import random
import math


class SimulatedAnnealing(object):

    def __init__(self, problem):
        self.problem = problem
        self.problem_solver(problem.initial_state())
