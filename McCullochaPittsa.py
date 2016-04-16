from __future__ import division

#Neuron McCullocha-Pittsa

def pitsa(x):
    if x >= 0:
        return 1
    else:
        return 0

class neuron(object):
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias


    def mcp(self, inputs):
        y = sum([i*w for (i,w) in zip(inputs, self.weights)])
        return pitsa(y+self.bias)

# run classes and functions
if __name__ == '__main__':
    neuronNOT = neuron([-1/2, 1/3],0)
    neuronAND = neuron([1/3, 1/3, -1/2],0)
    neuronOR = neuron([1/2, 1/2, -1/3],0)
    neuronNAND= neuron([-1/3, -1/3, 1/2],0)

    print 'not(0)', neuronNOT.mcp([0,1])
    print 'not(1)', neuronNOT.mcp([1,1])
    print ' '
    print 'and(0,0)', neuronAND.mcp([0, 0, 1])
    print 'and(0,1)', neuronAND.mcp([0, 1, 1])
    print 'and(1,0)', neuronAND.mcp([1, 0, 1])
    print 'and(1,1)', neuronAND.mcp([1, 1, 1])
    print ' '
    print 'nand(0,0)', neuronNAND.mcp([0, 0, 1])
    print 'nand(0,1)', neuronNAND.mcp([0, 1, 1])
    print 'nand(1,0)', neuronNAND.mcp([1, 0, 1])
    print 'nand(1,1)', neuronNAND.mcp([1, 1, 1])
    print ' '
    print 'or(0,0)', neuronOR.mcp([0, 0, 1])
    print 'or(0,1)', neuronOR.mcp([0, 1, 1])
    print 'or(1,0)', neuronOR.mcp([1, 0, 1])
    print 'or(1,1)', neuronOR.mcp([1, 1, 1])