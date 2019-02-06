import random
import Image
import numpy as np
import random



class DNA:
    def __init__(self, target, limit=None, genes=None):
        # for faster evolution, you can limit the range of the gene values. This is something to consider
        # if the target image is large.
        self.bound = False
        if limit is not None:
            self.limit = limit
            self.bound = True
        self.target = target
        self.width = target.width
        self.height = target.height
        self.fitness = 0
        # if no genes are passed, randomly create the genes
        if genes == None:
            self.genes = [[[0, 0, 0] for y in range(self.height)] for x in range(self.width)]
            for x in range(self.width):
                for y in range(self.height):
                    for z in range(3):
                        if self.bound:
                            # limit the range
                            rand = random.randint(self.target.array[x][y][z] - limit, self.target.array[x][y][z] + limit)
                            if rand < 0:
                                # makes sure rand is at least = 0 since the lowest possible RGB value is 0
                                rand = rand - rand
                            elif rand > 255:
                                # makes sure rand is at most = 255 since the highest possible RGB value is 255
                                rand = rand - (rand - 255)
                        else:
                            rand = random.randint(0, 255)
                        self.genes[x][y][z] = rand
            # transform the genes list into a numpy array so it can later be turned into an image
            self.array = np.array(self.genes, dtype=np.uint8)
        else:
            self.genes = genes
            # transform the genes list into a numpy array so it can later be turned into an image
            self.array = np.array(self.genes, dtype=np.uint8)

    def show(self):
        # transform the array into an image
        picture = Image.fromarray(self.array)
        picture.show()

    def calc_fitness(self):
        score = 0
        # checks every element in the randomly created array. If it is equal to the 
        # element of the target array in the same location, its score increases by 1.
        for x in range(len(self.array)):
            for y in range(len(self.array[x])):
                for z in range(3):
                    if self.array[x][y][z] == self.target.array[x][y][z]:
                        score += 1
        # normalize the fitness score. Multiply the target size by 3 since there
        # are 3 values (RGB values) in every index of the target.
        self.fitness = score / (self.target.size * 3)

    def crossover(self, other):
        # create a child DNA object from self and other
        genes = [[[0, 0, 0] for y in range(self.height)] for x in range(self.width)]
        switch = 0
        for x in range(self.width):
            for y in range(self.height):
                for z in range(3):
                    # if the value in one of the parent arrays is the same as the one in the
                    # target array, pass that specific value to the child array rather than switching
                    # between the parents.
                    if self.array[x][y][z] == self.target.array[x][y][z]:
                        genes[x][y][z] = self.array[x][y][z]
                    elif other.array[x][y][z] == self.target.array[x][y][z]:
                        genes[x][y][z] = other.array[x][y][z]
                    else:
                        if switch == 0:
                            switch = 1
                            genes[x][y][z] = self.genes[x][y][z]
                        else:
                            genes[x][y][z] = other.genes[x][y][z]
                            switch = 0
        return DNA(self.target, None, genes)

    def mutate(self, mutation_rate):
        for x in range(self.width):
            for y in range(self.height):
                for z in range(3):
                    # based on the mutation rate, mutate a random RGB value
                    if random.uniform(0,1) < mutation_rate:
                        # if the RGB value to be mutated is equal to the target RGB value, don't mutate it.
                        if self.array[x][y][z] != self.target.array[x][y][z]:
                            self.array[x][y][z] = (random.randint(0, 255))
            
         