from DNA import *
import operator
import random

class Population:
    def __init__(self, target, mutation_rate, population_size, bound=None):
        self.mutation_rate = mutation_rate
        self.population_size = population_size
        self.target = target
        self.generation = 1
        self.population = []
        self.fitness_scores = {}
        self.finished = False

        print("Building Population...")
        
        # create a population full of DNA objects 
        for x in range(self.population_size):
            self.population.append(DNA(target, bound))
        
        print("Population Built.\n")

        print("Generation: ", self.generation)

        self.mating_pool = []

    def calc_fitness(self):
        if self.generation != 1:
            for x in range(len(self.population)):
                if self.fitness_scores[x] == 1:
                    self.finished = True
                    self.population[x].show()
                    break
        if not self.finished:
            print("Calculating Fitness...")

            # for each memeber, calculate its fitness score.
            for member in self.population:
                member.calc_fitness()

            for x in range(len(self.population)):
                self.fitness_scores[x] = self.population[x].fitness

            print("Fitness Calculated.\n")

    def natural_selection(self):

        print("Performing Natural Selection...")

        # add each fitness score to a dictionary with its location in the population as the key.
        
        
        # sort the fitness_scores dictionary with respect to the fitness scores and reverse the list
        # so that the first members are the ones with the highest fitness scores.
        fitness_scores_sorted = list(reversed(sorted(self.fitness_scores.items(), key=operator.itemgetter(1))))

        print("Natural Selection Complete.\n")

        print("Member with Highest Fitness Score, Score: ", fitness_scores_sorted[0])
        # the mating pool consists of the best half of the population
        self.mating_pool = fitness_scores_sorted[:int(len(fitness_scores_sorted) / 2)]

        # gets the index of which DNA member in the population should carry on
        newpool = []
        for x in range(len(self.mating_pool)):
            newpool.append(self.mating_pool[x][0])
        
        # create a temporary list to hold the population members
        temp = []
        for x in newpool:
            temp.append(self.population[x])
        self.mating_pool = temp

    def crossover(self):
        top = len(self.mating_pool)

        print("Perfomring Crossover...")
        
        count = len(self.population)
        # empty the population list
        self.population = []
        for _ in range(count):
            rand1 = random.randint(0, top - 1)
            rand2 = random.randint(0, top - 1)
            # make sure you get two different random numbers so you dont crossover the same two population members
            while rand1 == rand2:
                rand2 = random.randint(0, top - 1)
            # mate two mating pool members to get a new population member
            self.population.append(self.mating_pool[rand1].crossover(self.mating_pool[rand2]))

        print("Crossover Complete.\n")

        # after crossover is complete, the next generation has been made.
        self.generation += 1
        print("Generation: ", self.generation)

    def mutate(self):
        print("Mutating...")

        # mutate each member of the population.
        for member in self.population:
            member.mutate(self.mutation_rate)
        
        print("Mutation Complete.\n")

    def evolve(self):
        # only finished when one of the population members successfully becomes the target image
        while True:
            self.calc_fitness()
            if self.finished:
                break
            self.natural_selection()
            self.crossover()
            self.mutate()
            

