class XOR():
    def __init__(self):
        pass
    def inputs(self):
        inputs = [[0,0],[0,1],[1,0],[1,1]]
        return inputs
    def test(self,input_num,real_outputs, outputs, genome):
        i = input_num
        for a in range(len(outputs)):
            val = outputs[a]
            if val < 0.5:
                real_output = 0
            elif outputs[a] >= 0.5:
                real_output = 1
            if real_output == real_outputs[i]:
                v = (val - real_outputs[i]) ** 2
                genome.fitness -= v
                genome.right += 1
            else:
                v = (val - real_outputs[i]) ** 2
                genome.fitness -= v


