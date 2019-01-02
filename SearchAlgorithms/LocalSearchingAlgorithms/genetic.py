import random
import collections
import operator
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3


class Genetic:

    def __init__(self, problem, generation_size, population_size, tournament_size, mutation_size):
        self.chromosomes = []
        self.new_chromosome = []
        self.best_evaluation = []
        self.worst_evaluation = []
        self.average_evaluation = []
        self.fitness_map = []

        self.problem = problem
        self.generation_size = generation_size
        self.population_size = population_size
        self.tournament_size = tournament_size
        self.mutation_size = mutation_size

        self.problem.initial_state()
        self.do_genetic()

    def make_population(self):
        for p in range(self.population_size):
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

        self.fitness_map.append(((all_edge - same_color_edge) // 2) / (all_edge // 2))

    def single_fitness(self, chromosome):
        graph = self.problem.cgraph.graph
        all_edge = 0
        same_color_edge = 0
        for g in graph:
            for n in graph[g]:
                all_edge += 1
                if chromosome[n] == chromosome[g]:
                    same_color_edge += 1

        return ((all_edge - same_color_edge) // 2) / (all_edge // 2)

    def tournament(self):
        tournament_parents = []
        temp_tournament_parents = []
        chosen_parents = []
        best_chosen = []
        best_chosen_fitness = []
        parent_size = self.population_size // self.tournament_size
        count = 0
        t_count = 0

        randoms = [i for i in range(self.population_size)]
        while count != parent_size:
            while t_count != self.tournament_size:
                rc = random.choice(randoms)
                state = self.chromosomes[rc]
                # if state not in tournament_parents:
                temp_tournament_parents.append(state)
                randoms.remove(rc)
                t_count += 1

            for y in temp_tournament_parents:
                best_chosen.append(y)
                best_chosen_fitness.append(self.single_fitness(y))

            chosen_parents.append(best_chosen[best_chosen_fitness.index(max(best_chosen_fitness))])
            tournament_parents += temp_tournament_parents
            temp_tournament_parents.clear()
            best_chosen.clear()
            best_chosen_fitness.clear()
            count += 1
            t_count = 0

        return chosen_parents

        # randoms = []
        # parents = []
        # parent_size = self.population_size // self.tournament_size
        # count = 0
        #
        # while count != parent_size:
        #     r = random.randrange(parent_size)
        #     if r not in randoms:
        #         parents.append(self.chromosomes[r])
        #         randoms.append(r)
        #         count += 1
        #
        # return parents


    def new_generation(self, parents):
        for i in range(self.population_size):
            r1 = random.randrange(parents.__len__())
            r2 = random.randrange(parents.__len__())
            self.new_chromosome.append(self.crossover(parents[r1], parents[r2]))

    def crossover(self, chromosome1, chromosome2):
        gen_list = list(chromosome1.keys()) + list(chromosome2.keys())
        color_list = list(chromosome1.values()) + list(chromosome2.values())
        temp_chromosome = collections.defaultdict(list)

        for c in range(len(gen_list)):
            if c % 2 == 0:
                temp_chromosome[gen_list[c]] = color_list[c]

        new_chromosome = dict(collections.OrderedDict(sorted(temp_chromosome.items())))

        return collections.defaultdict(list, new_chromosome)

    def mutation(self):
        muted_genomes = self.population_size * self.problem.cgraph.graph.__len__() * self.mutation_size
        for g in range(int(muted_genomes) + 1):
            r1 = random.randrange(self.chromosomes.__len__())
            r2 = random.randrange(self.chromosomes[r1].__len__())

            while True:
                r3 = random.randrange(self.problem.color_size)
                if r3 != self.chromosomes[r1][r2]:
                    self.chromosomes[r1][r2] = r3
                    break

        for c in self.chromosomes:
            self.fitness(c)

    def evaluation(self):
        self.best_evaluation.append(max(self.fitness_map))
        self.worst_evaluation.append(min(self.fitness_map))
        self.average_evaluation.append(sum(self.fitness_map) / self.fitness_map.__len__())

    def ploting(self):
        plt3.plot(self.best_evaluation, label='Best', color='green')
        plt3.legend()
        # plt1.title('Best Evaluations In Each Generation')
        # plt1.xlabel('Generation')
        # plt1.ylabel('Evaluation')
        # plt1.minorticks_on()
        # plt1.grid()
        # plt1.show()

        plt3.plot(self.worst_evaluation, label='Worst', color='red')
        plt3.legend()
        # plt2.title('Worst Evaluations In Each Generation')
        # plt2.xlabel('Generation')
        # plt2.ylabel('Evaluation')
        # plt2.minorticks_on()
        # plt2.grid()
        # plt2.show()

        plt3.plot(self.average_evaluation, label='Average', color='blue')
        plt3.legend()
        plt3.title('Evaluations In Each Generation')
        plt3.xlabel('Generation')
        plt3.ylabel('Evaluation')
        plt3.minorticks_on()
        plt3.grid()
        plt3.show()

    def do_genetic(self):
        for i in range(self.generation_size):
            if i % 1000 == 0:
                print(f'*******************************************generation {i}')
            if i != 0:
                self.chromosomes = self.new_chromosome.copy()
                self.new_chromosome.clear()
            else:
                self.make_population()

            self.new_generation(self.tournament())
            self.mutation()
            self.evaluation()

        print(f'Number of colors: {self.problem.color_size}')
        print(f'Number of generations: {self.generation_size}')
        print(f'Population size: {self.population_size}')
        print(f'Tournament size: {self.tournament_size}')
        print(f'Mutation size: {self.mutation_size}')
        print('......')
        print(f'Best evaluation: {max(self.best_evaluation)}')
        print(f'Worst evaluation: {min(self.worst_evaluation)}')
        print(f'Average evaluation: {sum(self.average_evaluation) / self.average_evaluation.__len__()}')
        self.ploting()
