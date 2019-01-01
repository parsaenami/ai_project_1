

class Genetic:

    def __init__(self, problem, population_size, tornument_size, mutation_size):
        self.populations = []
        self.new_chromosome = []

        self.problem = problem
        self.population_size = population_size
        self.tornument_size = tornument_size
        self.mutation_size = mutation_size
        # self.function

    # def make_population(self, population_size):
    #     for p in range(population_size):

