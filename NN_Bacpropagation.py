import math

import numpy as np

def sigmoid(x):
    return 1 / (1+np.exp(-x))

training_inputs = np.array([[0,0,1],
                           [1,1,1],
                           [1,0,1],
                           [0,1,1]])

training_outputs = np.array([[0,1,1,0]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((3,1)) - 1

print("Tasodifiy ishga tushiruvchilar:")
print(synaptic_weights)


for i in range(20):
    input_layer = training_inputs
    outputs = sigmoid( np.dot(input_layer, synaptic_weights) )

    err = training_outputs - outputs
    print('xatoliq\n',err)
    adjustments = np.dot( input_layer.T, err * (outputs * (1 - outputs) ) )
    print('adjustment\n',adjustments)
    synaptic_weights += adjustments
    print('weight\n',synaptic_weights)

print( "Mashg'ulotdan keyin:" )
print(synaptic_weights)

print("Mashg'ulotdan keyingi natija:")
print(outputs)

# TEST
new_inputs = np.array([2.30,2,2])
outputs = sigmoid( np.dot(new_inputs, synaptic_weights) )

print("Yangi holat:")
print(outputs)
print(math.pow(28,20))