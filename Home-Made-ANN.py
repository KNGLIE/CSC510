import numpy as np


class NeuralNetwork:
    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1], 8)
        self.weights2 = np.random.rand(8, 4)
        self.weights3 = np.random.rand(4, 1)
        self.y = y
        self.output = np.zeros(y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.layer2 = sigmoid(np.dot(self.layer1, self.weights2))
        self.output = sigmoid(np.dot(self.layer2, self.weights3))
        return self.output

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights3, weights2 and weights1
        d_weights3 = np.dot(self.layer2.T, (2 * (self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights2 = np.dot(self.layer1.T, (np.dot(2 * (self.y - self.output) * sigmoid_derivative(self.output),
                                                   self.weights3.T) * sigmoid_derivative(self.layer2)))
        d_weights1 = np.dot(self.input.T, (np.dot(
            np.dot(2 * (self.y - self.output) * sigmoid_derivative(self.output), self.weights3.T) * sigmoid_derivative(
                self.layer2), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2
        self.weights3 += d_weights3


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


if __name__ == "__main__":
    X = np.array([[0, 0, 1],
                  [0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]])
    y = np.array([[0], [1], [1], [0]])
    nn = NeuralNetwork(X, y)

    for i in range(2000):
        nn.feedforward()
        nn.backprop()

    print(nn.output)

# This neural network has 3 layers,
# an input layer, a hidden layer with 8 neurons,
# another hidden layer with 4 neurons,
# and an output layer with 1 neuron.
# The weights for the connections between
# the layers are randomly initialized using
# the numpy random function. The sigmoid
# function and its derivative are used as the
# activation functions for the neurons.
# The feedforward and backpropagation functions
# are implemented, which are used to make predictions
# and update the network's weights and biases during training.
