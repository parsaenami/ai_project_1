import random
import collections


class Genetic:

    def __init__(self, problem, generation_size, population_size, tournament_size, mutation_size):
        self.chromosomes = []
        self.new_chromosome = []
        self.fitness_map = {}

        self.problem = problem
        self.generation_size = generation_size
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

    def new_generation(self):
        for i in range(self.population_size):
            r1 = random.randrange(self.population_size)
            r2 = random.randrange(self.population_size)
            self.new_chromosome.append(self.crossover(self.chromosomes[r1], self.chromosomes[r2]))

        self.chromosomes = self.new_chromosome.copy()
        self.new_chromosome.clear()

    def crossover(self, chromosome1, chromosome2):
        gen_list = list(chromosome1.keys()) + list(chromosome2.keys())
        color_list = list(chromosome1.values()) + list(chromosome2.values())
        temp_chromosome = {}

        for c in range(len(gen_list)):
            if c % 2 == 0:
                temp_chromosome[gen_list[c]] = color_list[c]

        new_chromosome = dict(collections.OrderedDict(sorted(temp_chromosome.items())))

        return new_chromosome