import random


class Genetic:

    def __init__(self, problem, population_size, tournament_size, mutation_size):
        self.chromosomes = []
        self.new_chromosome = []
        self.fitness_map = {}

        self.problem = problem
        self.population_size = population_size
        self.tournament_size = tournament_size
        self.mutation_size = mutation_size
        # self.function

    def make_population(self, population_size):
        for p in range(population_size):
            self.chromosomes.append(self.problem.new_state())

    def fitness(self, chromosome):
        graph = self.problem.cgraph.graph
        all_edge = 0
        same_color_edge = 0
        for g in graph:
            for n in graph[g]:
                all_edge += 1
                if chromosome[n] == chromosome[g]:
                    same_color_edge += 1

        self.fitness_map[chromosome] = ((all_edge - same_color_edge) // 2) / (all_edge // 2)

    def tournament(self, k):
        randoms = []
        parents = []
        parent_size = self.population_size // k
        count = 0

        while count != parent_size:
            r = random.randrange(parent_size)
            if r not in randoms:
                parents.append(self.chromosomes[r])
                randoms.append(r)
                count += 1

        return parents