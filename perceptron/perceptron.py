import numpy as np

def andPerceptron(x1, x2):
    return perceptron(np.array([x1, x2]), np.array([1, 1]), -1.9)

def nandPerceptron(x1, x2):
    return perceptron(np.array([x1, x2]), np.array([-1, -1]), 1.9)

def orPerceptron(x1, x2):
    return perceptron(np.array([x1, x2]), np.array([1, 1]), -0.9)

def xorPerceptron(x1, x2):
    neuron1 = nandPerceptron(x1, x2)
    neuron2 = orPerceptron(x1, x2)
    return andPerceptron(neuron1, neuron2)

def perceptron(neurons, weights, bias):
    if np.sum(neurons * weights) + bias <= 0:
        return 0;

    return 1

params = [
    {'x1': 0, 'x2': 0},
    {'x1': 1, 'x2': 0},
    {'x1': 0, 'x2': 1},
    {'x1': 1, 'x2': 1},
]

functionDefinitions = [
    {'name': 'andPerceptron' , 'func': andPerceptron},
    {'name': 'nandPerceptron' , 'func': nandPerceptron},
    {'name': 'orPerceptron' , 'func': orPerceptron},
    {'name': 'xorPerceptron' , 'func': xorPerceptron}
]

for v in functionDefinitions:
    print('\n' + v['name'] + '\n=====\n')

    for param in params:
        print('x1:' + str(param['x1']) + ' ' + 'x2:' + str(param['x2']) + ' res:' + str(v['func'](param['x1'], param['x2'])) + '\n')