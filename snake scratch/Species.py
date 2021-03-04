import random
from Genome import *
import copy
c1 = 1
c2 = 1
c3 = 3 # 3 for large pop size 1000+ while 0.4 for small pop size
distance_threshold = 4 # 3 for small pop size and 4 for large pop size
kill_precent = 0.8
extintion_gens = 15 #amount of generations a species will survive if its fitness does not improve

class Species():
    def __init__(self, rep):
        self.genomes = [rep]
        self.rep = rep
        self.fitness = 0
        self.new_genome_list = []
        self.genomes_best = []
        self.fit_best = False
        self.total_fitnesses = []
        self.offsprings = []
        self.gens_without_improvement = 0
        self.champion = None
    def cross_over(self ,genome1, genome2, system):
        genome1_bigger = False
        genome1.excess_genes = []
        genome1.excess_genes_innos = []
        genome2.excess_genes = []
        genome2.excess_genes_innos = []
        offspring_genome_connections = []
        offspring_genome_nodes = []
        offspring_genome_nodes_innos = []
        offspring_genome_connections_innos = []
        genome1_connections = genome1.best_connections
        genome2_connections = genome2.best_connections
        most_nodes = len(genome1_connections)
        least_nodes = len(genome2_connections)
        num_gen1 = 0
        num_gen2 = 0
        #function for adding nodes
        if genome1.fitness > genome2.fitness:
            for node in genome1.nodes:
                offspring_genome_nodes.append(node)
        elif genome1.fitness < genome2.fitness:
            for node in genome2.nodes:
                offspring_genome_nodes.append(node)

        elif genome1.fitness == genome2.fitness:
            for node in genome1.nodes:
                offspring_genome_nodes.append(node)
                offspring_genome_nodes_innos.append(node.innovation_number)

            for node in genome2.nodes:
                if node.innovation_number not in offspring_genome_nodes_innos:
                    offspring_genome_nodes_innos.append(node.innovation_number)
                    offspring_genome_nodes.append(node)

        #creating offspring connections
        while num_gen1 < len(genome1_connections) and num_gen2 < len(genome2_connections):
            if genome1_connections[num_gen1].innovation_number == genome2_connections[num_gen2].innovation_number:
                rand_num = random.randint(0,1)
                if rand_num == 0:
                    offspring_genome_connections.append(genome1_connections[num_gen1])
                    offspring_genome_connections_innos.append(genome2_connections[num_gen2].innovation_number)
                else:
                    offspring_genome_connections.append(genome2_connections[num_gen2])
                    offspring_genome_connections_innos.append(genome2_connections[num_gen2].innovation_number)
                genome1.similar_connections.append(genome1_connections[num_gen1])
                genome2.similar_connections.append(genome2_connections[num_gen2])
                num_gen2 += 1
                num_gen1 += 1
            elif genome1_connections[num_gen1].innovation_number > genome2_connections[num_gen2].innovation_number:
                genome2.disjoint_genes.append(genome2_connections[num_gen2])
                genome2.disjoint_genes_innos.append(genome2_connections[num_gen2].innovation_number)
                num_gen2 += 1
            elif genome2_connections[num_gen2].innovation_number > genome1_connections[num_gen1].innovation_number:
                genome1.disjoint_genes.append(genome1_connections[num_gen1])
                genome1.disjoint_genes_innos.append(genome1_connections[num_gen1].innovation_number)
                num_gen1 += 1
        #creting excess genes
        while num_gen1 < len(genome1_connections):
            genome1.excess_genes.append(genome1_connections[num_gen1])
            genome1.excess_genes_innos.append(genome1_connections[num_gen1].innovation_number)
            num_gen1 += 1
        #finish offspring with excess and disjoint genes
        if genome1.fitness > genome2.fitness:
            for i in range(len(genome1.excess_genes)):
                offspring_genome_connections.append(genome1.excess_genes[i])
            for i in range(len(genome1.disjoint_genes)):
                offspring_genome_connections.append(genome1.disjoint_genes[i])
        elif genome1.fitness < genome2.fitness:
            for i in range(len(genome2.excess_genes)):
                offspring_genome_connections.append(genome2.excess_genes[i])
            for i in range(len(genome2.disjoint_genes)):
                offspring_genome_connections.append(genome2.disjoint_genes[i])
        elif genome1.fitness == genome2.fitness:
            for i in range(len(genome1.excess_genes)):
                offspring_genome_connections.append(genome1.excess_genes[i])
            for i in range(len(genome1.disjoint_genes)):
                offspring_genome_connections.append(genome1.disjoint_genes[i])
            for i in range(len(genome2.excess_genes)):
                offspring_genome_connections.append(genome2.excess_genes[i])
            for i in range(len(genome2.disjoint_genes)):
                offspring_genome_connections.append(genome2.disjoint_genes[i])
        all = [genome1.excess_genes, genome1.disjoint_genes, genome2.excess_genes, genome2.disjoint_genes]
        all1 = [offspring_genome_connections, offspring_genome_connections_innos, offspring_genome_nodes]
        offspring = Genome(genome1.inputs,genome1.outputs, system)
        offspring.nodes = offspring_genome_nodes
        offspring.connections = offspring_genome_connections
        offspring.best_connections = offspring_genome_connections
        offspring.inno_number = len(offspring_genome_nodes)

        return offspring




    def distance(self, genome, system):
        genome.disjoint_genes.clear()
        genome.disjoint_genes_innos.clear()
        genome.excess_genes.clear()
        genome.disjoint_genes_innos.clear()
        self.rep.disjoint_genes.clear()
        self.rep.disjoint_genes_innos.clear()
        self.rep.excess_genes.clear()
        self.rep.disjoint_genes_innos.clear()
        def get(genome1, genome2):
            index_g1 = 0
            index_g2 = 0
            disjoint = 0
            excess = 0
            weight_diff = 0
            similar = 0
            while index_g1 < len(genome1.connections) and index_g2 < len(genome2.connections):
                in1 = genome1.connections[index_g1].innovation_number
                in2 = genome2.connections[index_g2].innovation_number

                c1_val = genome1.connections[index_g1].weight
                c2_val = genome2.connections[index_g2].weight
                if in1 == in2:
                    #similar
                    weight_diff += abs(c1_val - c2_val)
                    index_g2 +=1
                    index_g1 += 1
                    similar += 1
                elif in1 > in2:
                    #disjoint of b
                    disjoint += 1
                    index_g2 += 1
                else:
                    index_g1 += 1
                    disjoint += 1
            if similar != 0:
                weight_diff /= similar
            excess = len(genome1.connections) - index_g1
            N = len(genome1.connections)
            if N < 20:
                N = 1
            return weight_diff, excess, disjoint, N
        if len(genome.nodes) >= len(self.rep.nodes):
            weight_diff, excess, disjoint, N = get(genome, self.rep)
        else:
            weight_diff, excess, disjoint, N = get(self.rep, genome)

        Distance = ((c1 * excess)/ N) + ((c2* disjoint)/N) + (c3 * weight_diff )
        genome.similar_connections.clear()
        self.rep.similar_connections.clear()
        if Distance <= distance_threshold:
            return True
        else:
            return False


        # find distance then return True or false
        # true being it is compatible and false not being compatible

    def fitness_func(self):
        if self.champion == None:
            self.champion = self.genomes[0]
        score = 0
        fit = []
        for genome in self.genomes:
            score += genome.fitness
            fit.append(genome.fitness)
        if score != 0:
            self.fitness = score / len(self.genomes) #todo maybe change this
        else:
            self.fitness = 1
    def kill(self):
        #sorts fitness
        fitness_list = []
        kill_innos = []
        c_list = []
        self.new_genome_list = copy.deepcopy(self.genomes)
        for i in range(len(self.new_genome_list)):
            self.new_genome_list[i] = 0
        for genome in self.genomes:
            fitness_list.append(genome.fitness)
        fitness_list.sort()
        list2 = copy.deepcopy(fitness_list)
        for a in range(len(self.genomes)):
            for i in range(len(fitness_list)):
                if self.genomes[a].fitness == fitness_list[i]:
                    self.genomes[a].place = i
                    fitness_list[i] = 99999999
                    c_list.append([a,i])
                    break
        for i in range(len(c_list)):
            for a in range(len(self.genomes)):
                if a == c_list[i][0]:
                    self.genomes[a].place = c_list[i][1]
                    self.new_genome_list[self.genomes[a].place] = self.genomes[a]
        #kills by making a new list with everything except dead genomes
        len_genomes = len(self.new_genome_list)
        kill_num = math.floor(len_genomes * kill_precent)

        for i in range(len_genomes):
            if i <= kill_num:
                pass
            else:
                self.genomes_best.append(self.new_genome_list[i])
        #reset place
        for genome in self.genomes_best:
            genome.place = 0
        if kill_num == 0:
            return False
        else:
            return True
    def reproduce(self, amount_, system):
        parents = []
        offsprings = []
        offsprings_new = []
        sum_fitness = 0
        if len(self.genomes_best) != 1:
            for genome in self.genomes_best:
                sum_fitness += genome.fitness
            for genome in self.genomes_best:
               if genome.fitness <= 0:
                   continue
               # gets the amount each genome will reproduce
               genome.precent = genome.fitness / sum_fitness
            while len(offsprings) < len(self.genomes_best) // amount_ :
                for genome in self.genomes_best:
                   if random.random() <= genome.precent:
                       ran = random.randint(0,len(self.genomes_best) - 1)
                       genome1 = self.genomes_best[ran]
                       if len(genome.nodes) > len(genome1.nodes):
                           offspring = self.cross_over(genome,genome1, system)
                       else:
                           offspring = self.cross_over(genome1, genome, system)
                       offsprings.append(offspring)
        if len(offsprings) <= 1: # aka if there is one genome so it just keeps mutating that
            for i in range(int(amount_)):
                mutation = copy.deepcopy(self.genomes[0])
                for i in range(1):
                    mutation.mutate()
                offsprings.append(mutation)
        for i in range(int(amount_)):
            num = random.randint(0, len(offsprings) - 1)
            copy1 = copy.deepcopy(offsprings[num])
            copy1.mutate()
            offsprings_new.append(copy1)

        self.offsprings = offsprings_new
        return self.offsprings


