import math

data = [
    [5.1, 3.5, 'Setosa'],
    [6.0, 2.9, 'Versicolor'],
    [6.9, 3.1, 'Virginica']
]

test = [5.0, 3.4]

distances = []

for row in data:
    d = math.sqrt((row[0]-test[0])**2 + (row[1]-test[1])**2)
    distances.append((d, row[2]))

distances.sort()

print("Predicted Flower:", distances[0][1])
