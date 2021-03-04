from Gene import *
from System import *
from ConnectionGene import *
from HiddenNode import *
from XOR import *
from snake import *
import math
import random
import copy
import numpy as np
import math

PROBABILITY_MUTATE_LINK = 0.3  # .05 in smaller pop and 0.3 for large pop
PROBABILITY_MUTATE_NODE = 0.03
PROBABILITY_MUTATE_WEIGHTS = 0.8
PROBABILITY_MUTATE_WEIGHT_SHIFT = 0.9
PROBABILITY_MUTATE_WEIGHT_RANDOM = 0.1
PROBABILITY_MUTATE_TOGGLE_LINK = 0.0
WEIGHT_SHIFT_STRENGTH = 0.30

# creates brand new genome
class Genome():
    def __init__(self, inputs, outputs, system):
        self.system = system
        self.inputs = inputs
        self.outputs = outputs
        self.place = 0
        self.nodes = []
        self.connections = []
        # self.layer = 1
        # self.node_num = 1
        self.age = 0
        self.inno_number = 0
        self.encode()
        self.mutate()
        self.best_connections = copy.deepcopy(self.connections)
        for i in range(len(self.best_connections)):
            self.best_connections[i] = 0
        self.excess_genes = []
        self.excess_genes_innos = []
        self.disjoint_genes = []
        self.disjoint_genes_innos = []
        self.similar_connections = []
        self.fitness = 0
        self.right = 0
        self.amount_reproduce = 0
        self.precent = 0
        # self.check_connections()

    def check_connections(self):
        # fix multiple same innos in one genome
        run = 0
        while run <= len(self.connections):
            run += 1
            try:
                for i in range(len(self.connections)):
                    for a in range(len(self.connections)):
                        if a != i:
                            if self.connections[i].innovation_number == self.connections[a].innovation_number:
                                self.connections.pop(a)
                                run = 0
            except Exception:
                pass
        # sort innovation numbers
        self.best_connections = copy.deepcopy(self.connections)
        for i in range(len(self.best_connections)):
            self.best_connections[i] = 0
        c_list = []  # check list
        innos_list = []
        for connection in self.connections:
            innos_list.append(connection.innovation_number)
        innos_list.sort()
        for connection in self.connections:
            for i in range(len(innos_list)):
                if connection.innovation_number == innos_list[i]:
                    connection.place = i
                    innos_list[i] = 99999999999999999999999999999999  # make sure it cant be used again
                    c_list.append([connection.innovation_number, i])
        for i in range(len(c_list)):
            for connection in self.connections:
                if connection.innovation_number == c_list[i][0]:
                    connection.place = c_list[i][1]
                    self.best_connections[connection.place] = connection

    def more_connections_than_node(self):
        # if connection has a node that isnt in self.nodes
        for connection in self.connections:
            gene_to = connection.gene_to
            gene_from = connection.gene_from
            if len(self.nodes) < gene_from:
                self.inno_number += 1
                val = random.random()
                self.nodes.append(Gene(2, self.inno_number, val))
            if len(self.nodes) < gene_to:
                self.inno_number += 1
                val = random.random()
                self.nodes.append(Gene(2, self.inno_number, val))

    def random_val(self):
        val = random.uniform(-1, 1)
        return val

    def encode(self):
        for i in range(self.inputs):
            self.inno_number += 1
            # change weight from none to the value of the input
            self.nodes.append(Gene(1, self.inno_number, 0))
        for i in range(self.outputs):
            self.inno_number += 1
            self.nodes.append(Gene(3, self.inno_number, 1))

    def mutate(self):
        def connection_mutations():
            def mutate_link():
                for i in range(len(self.nodes) * 2):
                    # randomly sets node1 and node2
                    node1 = self.nodes[random.randint(0, len(self.nodes) - 1)]
                    node2 = self.nodes[random.randint(0, len(self.nodes) - 1)]
                    # if its an output ir bias go next
                    if node1.type == 3 or node1.type == 4:
                        continue
                    # if they're the same node or in the same layer go next
                    if node2 == node1 or node1.type == 1 and node2.type == 1:
                        continue
                    connection_name = f"{node1.innovation_number}_{node2.innovation_number}"
                    # if there are connections
                    is_con = False
                    if len(self.connections) != 0:
                        for connection in self.connections:
                            gene_to = connection.gene_to
                            gene_from = connection.gene_from
                            name1 = f"{gene_to}_{gene_from}"
                            name2 = f"{gene_from}_{gene_to}"
                            # if connection has not already been made
                            if connection_name == name1 or connection_name == name2:
                                is_con = True
                        if not(is_con):
                            innovation_number = self.system.set_inno_number(node1.innovation_number,
                                                                            node2.innovation_number)
                            weight = self.random_val()
                            if node1.y < node2.y:
                                self.connections.append(
                                    ConnectionGene(innovation_number, node1.innovation_number, node2.innovation_number,
                                                   True, weight))
                            else:
                                self.connections.append(
                                    ConnectionGene(innovation_number, node2.innovation_number, node1.innovation_number,
                                                   True, weight))
                            return None
                    else:
                        innovation_number = self.system.set_inno_number(node1.innovation_number,
                                                                        node2.innovation_number)
                        weight = self.random_val()
                        if node1.y < node2.y:
                            self.connections.append(
                                ConnectionGene(innovation_number, node1.innovation_number, node2.innovation_number,
                                               True, weight))
                        else:
                            self.connections.append(
                                ConnectionGene(innovation_number, node2.innovation_number, node1.innovation_number,
                                               True, weight))
                        return None

            def mutate_node():
                len1 = len(self.connections)
                if len1 > 0:
                    get_con = False
                    n = 0
                    # gets a connection that is that does not have the bias as its gene_from
                    while not (get_con):
                        n += 1
                        if len1 == 1:
                            ran_num = 0
                        else:
                            ran_num = random.randint(0, len1 - 1)  # gets random connection
                        if n > len1 * 3:
                            self.connections[ran_num].is_enabled = True
                        con = self.connections[ran_num]
                        active = con.is_enabled
                        gene_from = con.gene_from
                        gene_to = con.gene_to
                        try:
                            y1 = self.nodes[gene_from - 1].y
                            y2 = self.nodes[gene_to - 1].y
                        except Exception:
                            print('q')

                        if active and self.nodes[gene_from - 1].type != 4:
                            con.is_enabled = False
                            self.inno_number += 1
                            value = random.uniform(y1, y2)
                            self.nodes.append(Gene(2, self.inno_number, value))
                            og_weight = con.weight
                            gene_from1 = gene_from
                            gene_to1 = self.inno_number
                            gene_from2 = gene_to1
                            gene_to2 = con.gene_to
                            innovation_number = self.system.set_inno_number(gene_from1, gene_to1)
                            self.connections.append(ConnectionGene(innovation_number, gene_from1, gene_to1, True, 1))
                            innovation_number1 = self.system.set_inno_number(gene_from2, gene_to2)
                            self.connections.append(
                                ConnectionGene(innovation_number1, gene_from2, gene_to2, True, og_weight))
                            # self.node_num += 1
                            # if self.node_num > self.inputs:
                            #     self.node_num = 0
                            #     self.layer += 1
                            self.nodes[gene_from - 1].done = True
                            get_con = True
                            return None
                        else:
                            continue

            def mutate_weight_shift():
                for connection in self.connections: # slightly shift the value of the weights
                    # sees if genome can mutate
                    n = random.random()
                    if PROBABILITY_MUTATE_WEIGHT_SHIFT >= n:
                        pass
                    else:
                        continue

                    # gets age of gene_from to get weight_shift_stregth
                    # older the gene the less it should be changed because theoretically it should be better
                    # age = self.age
                    # val = 70 * (0.96) ** age
                    # WEIGHT_SHIFT_STRENGTH = val / 100
                    # changes the value of a weight by adding it to a random val
                    mult_num = self.random_val()
                    num = (mult_num * WEIGHT_SHIFT_STRENGTH)
                    add_ = connection.weight + num
                    if add_ >= 8 or add_ <= -8:  # cap of 2, -2
                        pass
                    else:
                        connection.weight = add_
            def mutate_weight_random(): # sets weights to a completely new value
                for connection in self.connections:
                    n = random.random()
                    if PROBABILITY_MUTATE_WEIGHT_RANDOM >= n:
                        pass
                    else:
                        continue
                    new_num = self.random_val()
                    connection.weight = new_num

            def toggle_link():
                len1 = len(self.connections)
                if len1 == 1:
                    ran_num = 0
                    on = self.connections[ran_num].is_enabled
                    if on:
                        self.connections[ran_num].is_enabled = False
                    else:
                        self.connections[ran_num].is_enabled = True
                elif len1 > 1:
                    ran_num = random.randint(0, len1)
                    on = self.connections[ran_num].is_enabled
                    if on:
                        self.connections[ran_num].is_enabled = False
                    else:
                        self.connections[ran_num].is_enabled = True

            # does mutations
            num1 = random.random()
            if PROBABILITY_MUTATE_LINK >= num1:
                mutate_link()
            num2 = random.random()
            if PROBABILITY_MUTATE_NODE >= num2:
                mutate_node()
            num5 = random.random()
            # if PROBABILITY_BIAS_MUTATE_LINK >= num5:
            #     bias_mutate_link()
            num4 = random.random()
            if PROBABILITY_MUTATE_WEIGHTS >= num4:
                mutate_weight_shift()
                mutate_weight_random()
            num6 = random.random()
            if PROBABILITY_MUTATE_TOGGLE_LINK >= num6:
                toggle_link()
            self.check_connections()
        def bias_mutations(): #mutations for bias
            def mutate_weight_shift():
                for node in self.nodes: # slightly shift the value of the weights
                    if node.type == 1: # if its a input it will not have a bias
                        continue
                    # sees if genome can mutate
                    n = random.random()
                    if PROBABILITY_MUTATE_WEIGHT_SHIFT >= n:
                        pass
                    else:
                        continue
                    # gets age of gene_from to get weight_shift_stregth
                    # older the gene the less it should be changed because theoretically it should be better
                    # age = self.age
                    # val = 70 * (0.96) ** age
                    # WEIGHT_SHIFT_STRENGTH = val / 100
                    # changes the value of a weight by adding it to a random val
                    mult_num = self.random_val()
                    num = (mult_num * WEIGHT_SHIFT_STRENGTH)
                    add_ = node.bias + num
                    if add_ >= 8 or add_ <= -8:  # cap of 8, -8
                        pass
                    else:
                        node.bias = add_
            def mutate_weight_random():

                # gives each bias a random value
                for node in self.nodes:
                    if node.type == 1:
                        continue
                    n = random.random()
                    if PROBABILITY_MUTATE_WEIGHT_RANDOM >= n:
                        pass
                    else:
                        continue
                    new_num = self.random_val()
                    node.bias = new_num

            num4 = random.random()
            if PROBABILITY_MUTATE_WEIGHTS >= num4:

                mutate_weight_shift()
                mutate_weight_random()
        connection_mutations()
        bias_mutations()

    def test_genome(self):
        self.more_connections_than_node()
        self.fitness = 0
        # xor = XOR()
        # inputs_needed = xor.inputs()
        #for snake
        main_snake(self)
        # inputs = main_snake.ma
        # output = self.calculate(inputs[i])

        # xor.test(i, outputs, output, self)


        #     print(val)
        # this is where ill actually test the genome and get its fitness

    def calculate(self, inputs):
        # self.check_connections()
        # reset all previous values
        for node in self.nodes:
            node.value = 0
            # set values of inputs
            for i in range(len(self.nodes)):
                if self.nodes[i].type == 1:
                    self.nodes[i].value = inputs[i]

                if self.nodes[i].type == 4:
                    self.nodes[i].value = 1

        # define simgoid function
        def sigmoid(x):
            try:
                sigmoid = 1 / (1 + np.exp(-x))  # try doing the modifed one in pdf
            except Exception:
                print("s")
            return sigmoid
        y_values = []
        #gives each connection the y value of its gene_From
        # puts y values in a list
        for connection in self.best_connections:
            gene_from = connection.gene_from
            connection.place = None
            connection.y = self.nodes[gene_from - 1].y
            y_values.append(connection.y)
        y_values.sort()
        # sorts connections from lowest y to highest y
        connections_sorted = copy.deepcopy(self.connections)
        for connection in self.best_connections:
            con_y = connection.y
            for i in range(len(y_values)):
                if con_y == y_values[i]:
                    connection.place = i
                    y_values[i] = 999999999999999 #makes that value unusable
                    connections_sorted[i] = connection
                    break
        # sets values of everything
        for connection in connections_sorted:
            is_enabled = connection.is_enabled
            if is_enabled:
                gene_from = connection.gene_from
                gene_to = connection.gene_to
                for i in range(len(self.nodes)):
                    if i == gene_from - 1:
                        # if its an input it sigmoides the value
                        if self.nodes[i].type == 1:
                            value_gene = (self.nodes[i].value)
                        else:
                            value_gene = sigmoid(self.nodes[i].value + self.nodes[i].bias)
                        break
                weight = connection.weight
                val = value_gene * weight
                for i in range(len(self.nodes)):
                    if i == gene_to - 1:
                        self.nodes[i].value += val
        outputs_ = []
        for node in self.nodes:
            if node.type == 3:
                outputs_.append(sigmoid(node.value + node.bias)) #todo MAYBE REMOVE SIGMOID DEPENDING ON PROBLEM
        return outputs_
