class ClassicSearchAlgorithm(object):

    def __init__(self, problem):
        self.problem = problem
        self.parent = {}
        self.parent_from_goal = {}
        self.memory = 0
