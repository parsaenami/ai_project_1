import random
import collections


class Genetic:

    def __init__(self, problem, generation_size, population_size, tournament_size, mutation_size):
        self.chromosomes = []
        self.new_chromosome = []
        self.best_evaluation = []
        self.worst_evaluation = []
        self.average_evaluation = []

        self.fitness_map = {}

        self.problem = problem
        self.generation_size = generation_size
        self.population_size = population_size
        self.tournament_size = tournament_size
        self.mutation_size = mutation_size

        self.do_genetic()

    def make_population(self):
        for p in range(self.population_size):
            self.chromosomes.append(self.problem.new_state())

        for c in self.chromosomes:
            self.fitness(c)

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

    def tournament(self):
        randoms = []
        parents = []
        parent_size = self.population_size // self.tournament_size
        count = 0

        while count != parent_size:
            r = random.randrange(parent_size)
            if r not in randoms:
                parents.append(self.chromosomes[r])
                randoms.append(r)
                count += 1

        return parents

    def new_generation(self, parents):
        for i in range(self.population_size):
            r1 = random.randrange(self.population_size)
            r2 = random.randrange(self.population_size)
            self.new_chromosome.append(self.crossover(parents[r1], parents[r2]))

    def crossover(self, chromosome1, chromosome2):
        gen_list = list(chromosome1.keys()) + list(chromosome2.keys())
        color_list = list(chromosome1.values()) + list(chromosome2.values())
        temp_chromosome = {}

        for c in range(len(gen_list)):
            if c % 2 == 0:
                temp_chromosome[gen_list[c]] = color_list[c]

        new_chromosome = dict(collections.OrderedDict(sorted(temp_chromosome.items())))

        return new_chromosome

    def mutation(self):
        muted_genomes = self.population_size * self.problem.cgraph.graph.__len__() * self.mutation_size
        for g in range(muted_genomes):
            r1 = random.randrange(self.chromosomes.__len__())
            r2 = random.randrange(self.chromosomes[r1])

            while True:
                r3 = random.randrange(self.chromosomes[r1][r2])
                if r3 != self.chromosomes[r1][r2]:
                    self.chromosomes[r1][r2] = r3
                    break

    def evaluation(self):
        self.best_evaluation.append(max(self.fitness_map.values()))
        self.worst_evaluation.append(min(self.fitness_map.values()))
        self.average_evaluation.append(sum(self.fitness_map.values()) / self.fitness_map.__len__())

    def do_genetic(self):
        for i in range(self.generation_size):
            if i != 0:
                self.chromosomes = self.new_chromosome.copy()
                self.new_chromosome.clear()

            self.make_population()
            self.new_generation(self.tournament())
            self.mutation()
            self.evaluation()

        print(f'Number of generations: {self.generation_size}')
        print(f'Population size: {self.population_size}')
        print(f'Tournament size: {self.tournament_size}')
        print(f'Mutation size: {self.mutation_size}')
        print('......')
        print(f'Best evaluation: {max(self.best_evaluation)}')
        print(f'Worst evaluation: {min(self.worst_evaluation)}')
        print(f'Average evaluation: {sum(self.average_evaluation) / self.average_evaluation.__len__()}')