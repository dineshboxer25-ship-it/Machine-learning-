import math

# Sample dataset
X = [1, 2, 3, 4, 5]
Y = [0, 0, 0, 1, 1]

# Parameters
w = 1
b = -3

# Sigmoid Function
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

print("Input\tProbability\tPrediction")

for x in X:
    z = w * x + b
    prob = sigmoid(z)

    if prob >= 0.5:
        prediction = 1
    else:
        prediction = 0

    print(x, "\t", round(prob, 4), "\t\t", prediction)
