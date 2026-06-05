import numpy as np

# Input Dataset (XOR)
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])

# Expected Output
Y = np.array([[0],
              [1],
              [1],
              [0]])

# Sigmoid Function
def sigmoid(x):
    return 1/(1+np.exp(-x))

# Derivative of Sigmoid
def sigmoid_derivative(x):
    return x*(1-x)

# Initialize weights randomly
input_layer_neurons = 2
hidden_layer_neurons = 2
output_neurons = 1

hidden_weights = np.random.uniform(size=(input_layer_neurons,
                                         hidden_layer_neurons))
hidden_bias = np.random.uniform(size=(1, hidden_layer_neurons))

output_weights = np.random.uniform(size=(hidden_layer_neurons,
                                         output_neurons))
output_bias = np.random.uniform(size=(1, output_neurons))

learning_rate = 0.5

# Training
for epoch in range(5000):

    hidden_layer_input = np.dot(X, hidden_weights)
    hidden_layer_input += hidden_bias
    hidden_layer_output = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_output,
                                output_weights)
    output_layer_input += output_bias
    predicted_output = sigmoid(output_layer_input)

    error = Y - predicted_output

    d_predicted_output = error * sigmoid_derivative(predicted_output)

    error_hidden_layer = d_predicted_output.dot(output_weights.T)
    d_hidden_layer = error_hidden_layer * \
                     sigmoid_derivative(hidden_layer_output)

    output_weights += hidden_layer_output.T.dot(
                      d_predicted_output) * learning_rate
    output_bias += np.sum(d_predicted_output,
                          axis=0, keepdims=True) * learning_rate

    hidden_weights += X.T.dot(d_hidden_layer) * learning_rate
    hidden_bias += np.sum(d_hidden_layer,
                          axis=0, keepdims=True) * learning_rate

print("Predicted Output:")
print(np.round(predicted_output))
