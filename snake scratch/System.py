from Genome import *
class System():
    def __init__(self):
        self.innovation_number_connection = 0
        self.connections = []
    def set_inno_number(self, from_, to_ ):
        fromto = str(from_) + "_" + str(to_)
        for i in range(len(self.connections)):
            if fromto in self.connections[i]:
                if self.connections[i][0] == fromto:
                    return i + 1

        else:
            self.innovation_number_connection += 1
            self.connections.append([fromto, self.innovation_number_connection])
            return self.innovation_number_connection

