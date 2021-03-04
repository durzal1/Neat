import random
class Gene():
    # type = input, hidden, or output or bias
    #          1        2        3        4
    def __init__(self, type, innovation_number, y):
        self.type = type
        self.innovation_number = innovation_number
        self.y = y
        self.sigmoid_value = 0
        self.done = False
        if type != 1:
            self.bias = random.uniform(-2,2)

