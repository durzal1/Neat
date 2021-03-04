from HiddenNode import  *
from ConnectionGene import *
from Gene import *
from System import *
from Genome import *
from Species import *
import time
import math
import pickle
import numpy as np
import random
yes = True

"""
extra features
1) interspecies reproduction
"""
# gets inputs
inputs1 = [0,0]
inputs2 = [0,1]
inputs3 = [1,0]
inputs4 = [1,1]
all_inputs = [[0], [0], [0], [0]]
inputs = [inputs1, inputs2, inputs3, inputs4]
index = []
while len(index) != len(inputs):
    num = random.randint(0,len(inputs) - 1)
    if num not in index:
        index.append(num)
for i in range(len(index)):
    all_inputs[i] = inputs[index[i] - 1]
true_outputs = [[0],[0],[0],[0]]
for i in range(len(all_inputs)):
    if all_inputs[i] == [0,0]:
        true_outputs[i] = 0
    elif all_inputs[i] == [0,1]:
        true_outputs[i] = 1
    elif all_inputs[i] == [1,0]:
        true_outputs[i] = 1
    elif all_inputs[i] == [1,1]:
        true_outputs[i] = 0




#
# pickle_in = open("champ.pickle", "rb")
# genome = pickle.load(pickle_in)
# print(genome)
# genome.test_genome(all_inputs, true_outputs)


precent_change = 10
class Neat():
    generation = 0
    species = []
    fits = []
    champion = None
    def main(self, inputs, outputs, pop_size):
        #this if for the 0th generation
        self.pop_size = pop_size
        self.outputs = outputs
        input_size = (inputs)
        self.genomes = []
        for i in range(pop_size):
            genome = Genome(input_size, outputs, System_main)
            self.genomes.append(genome)
        for genome in self.genomes:
            for i in range(1):
                genome.mutate()
            genome.test_genome()       # tests genome in testing environment
        self.evolve()
    def evolve(self):
        run = True
        while run:
            self.selection()
            self.sort()
            self.reproduce()
            self.test()
            self.generation += 1
            fit = []
            # if self.generation == 10:
            #     print('g')
            for genome in self.genomes:
                if genome.right > 3:
                    print("WORKED") #todo test with
                    pickle_out = open("genome.pickle", "wb")
                    pickle.dump(genome, pickle_out)
                elif genome.fitness <= 2:
                    # print(self.genomes[i].fitness)
                    pass
                genome.place = 0
                genome.similar_connections.clear()
                fit.append(genome.fitness)
            fit.sort()
            #finds best genome
            for genome in self.genomes:
                if genome.fitness == fit[-1]:
                    #sees if its the best the neural network has ever created
                    if self.champion == None:
                        self.champion = genome
                    else:
                        if genome.fitness > self.champion.fitness:
                            self.champion = genome
            self.fits.append(fit[-1])
            v = 0
            for fit_ in self.fits:
                v += fit_
            v = v/ len(self.fits)
            print(self.generation, len(self.species), fit[-1], v)
            # pickle_out = open("champ.pickle", "wb")
            # pickle.dump(self.champion, pickle_out)
    def test(self):
        # run = True
        for i in range(1):
            for genome_ in self.genomes:
                genome_.fitness = 0
                genome_.test_genome()
    def selection(self):
        #sorts genomes into species and if their isnt one that is good for it, it will create a new one.
        if len(self.species) != 0:
            for i in range(len(self.genomes)):
                if i != 0:
                    in_one = False
                    try:
                        for species_ in self.species:
                            rep = species_.rep
                            val = species_.distance(self.genomes[i],System_main)  # if return true then add it to the species
                            if val == True:  # if false it will go through the other species and if nothing works
                                species_.genomes.append(self.genomes[i])
                                in_one = True
                                break                 # it will create a new species.
                            else:
                                pass
                        if not(in_one):
                            self.species.append(Species(self.genomes[i]))
                    except Exception:
                        print("Fa")

        else:
            species = Species(self.genomes[0])
            self.species.append(species)
            for i in range(len(self.genomes)):
                if i != 0:
                    in_one = False
                    for species_ in self.species:
                        rep = species_.rep
                        val = species_.distance(self.genomes[i],
                                                System_main)  # if return true then add it to the species
                        if val == True:  # if false it will go through the other species and if nothing works
                            species_.genomes.append(self.genomes[i])
                            in_one = True
                            break  # it will create a new species.
                        else:
                            pass
                    if not (in_one):
                        self.species.append(Species(self.genomes[i]))

    def sort(self):
        # gets fitness and kills a precentage of the genomes | kills species that are extinct
        dead_genomes = []
        for i in range(len(self.species)):
            self.species[i].fitness_func()
            if self.species[i].kill() == False:
                dead_genomes.append(self.species[i])
        for i in range(len(dead_genomes)):
            self.species.remove(dead_genomes[i])

        # finds species with highest fitness
        fit = []
        for species in self.species:
            fit.append(species.fitness)
        fit_max = max(fit)
        for species in self.species:
            if species.fitness == fit_max:
                species.fit_best = True
    def reproduce(self):
        # reproduces in each species
        self.genomes.clear()
        sum_fitness = 0
        for species in self.species:
            sum_fitness += species.fitness
        for species in self.species:
            #gets precent of how much of the population will come from that species
            share = species.fitness / sum_fitness
            amount = math.ceil(share * self.pop_size)
            reproduce_amount = amount * 0.75
            offsprings = species.reproduce(reproduce_amount, System_main)
            for offspring in offsprings:
                self.genomes.append(offspring)
            #gets offspring that will came from mutation and not crossover
            mutate_share = amount
            amount_mutate = mutate_share * 0.25
            for i in range(round(amount_mutate)):
                    new = copy.deepcopy(species.champion)
                    new.mutate()
                    self.genomes.append(new)

        #gets the rep and best genome for each species
        for species in self.species:
            fit = []
            num = random.randint(0,len(species.genomes))
            for i in range(len(species.genomes)):
                if i == num:
                    species.rep = species.genomes[i]
                fit.append(species.genomes[i].fitness)
            fit.sort()
            for i in range(len(species.genomes)):
                if species.genomes[i].fitness == fit[-1]:
                    best = species.genomes[i]
                    if best.fitness > species.champion.fitness:
                        species.champion = best
                    species.genomes[i].fitness = 0
            #sees if species improved
            improved = False
            for fitness in species.total_fitnesses:
                if species.fitness > fitness:
                    improved = True
            if improved == True:
                species.gens_without_improvement = 0
            else:
                species.gens_without_improvement += 1
            species.total_fitnesses.append(species.fitness)
            #reset everything in the species
            species.genomes.clear()
            species.genomes.append(species.champion) # adds champ to the species again
            species.genomes_best.clear()
            species.new_genome_list.clear()
            species.offsprings.clear()
            species.fit_best = False
            species.fitness = 0
        #adds age to each gene and sets fitness to 0
        for genome in self.genomes:
            genome.fitness = 0
            genome.age += 1















neat = Neat()
neat.main(4, 4, 1000)