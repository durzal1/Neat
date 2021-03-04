from System import *

System_main = System()


class ConnectionGene():
    # y is which output neuron it is designated to
    def __init__(self, innovation_number, gene_from, gene_to, is_enabled, weight):
        self.innovation_number = innovation_number
        self.gene_from = gene_from
        self.gene_to = gene_to
        self.is_enabled = is_enabled
        self.weight =weight
        self.place = None
        self.y = None


