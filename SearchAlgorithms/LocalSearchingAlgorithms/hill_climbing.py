import random

class HillClimbing(object):

    def __init__(self, problem, type='greedy'):
        self.problem = problem
        self.type = type
        self.problem_solver(problem.initial_state())

