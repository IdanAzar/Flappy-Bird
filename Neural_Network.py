import numpy as np


class NeuralNetwork:
    @staticmethod
    def sigmoid(inputs):
        return 1.0 / (1.0 + np.exp(-inputs))

    @staticmethod
    def relu(inputs):
        return np.maximum(0, inputs)

    def __init__(self):

        self.model_architecture = [
            {"input_dim": 3, "current_dim": 8, "activation": "relu"},
            {"input_dim": 8, "current_dim": 8, "activation": "relu"},
            {"input_dim": 8, "current_dim": 2, "activation": "relu"},  # output Layer
        ]
        self.model = {}
        self.activation_dict = {"relu": self.relu, "sigmoid": self.sigmoid}
        self.init_layers()

    def init_layers(self, seed=99):
        np.random.seed(seed)
        for i, layer in enumerate(self.model_architecture):
            # Number the layers from 1 because we don't include the input layer in model
            index = str(i + 1)
            layer_input_dim = layer['input_dim']
            layer_current_dim = layer['current_dim']
            # we want matrix that have size of [layer_current_dim] on [layer_input_dim] and because of that we
            self.model['w' + index] = np.random.randn(
                layer_current_dim, layer_input_dim) * 0.1
            self.model['b' + index] = np.random.randn(
                layer_current_dim, 1)

    def calculate(self, inputs):
        neurons = inputs
        for i, layer in enumerate(self.model_architecture):
            index = str(i + 1)
            prev_neurons = neurons
            # Get information of current layer
            activation = self.activation_dict[layer['activation']]
            weights = self.model['w' + index]
            biases = self.model['b' + index]
            neurons = self.forward(prev_neurons, weights, biases, activation)
        return neurons

    @staticmethod
    def forward(prev_neurons, weights, biases, activation):
        z = np.dot(weights, prev_neurons) + biases
        return activation(z)

    def mutation(self, model, mutation_percent):
        high = 1 + mutation_percent
        low = 1 - mutation_percent
        rnd_range = high - low
        for key in self.model:
            # creating numpy array of random numbers with the same size of model[key]
            random_values = np.random.randn(*model[key].shape) * rnd_range + low
            self.model[key] = np.multiply(model[key], random_values)
