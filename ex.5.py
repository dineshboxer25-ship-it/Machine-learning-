# K-NN without sklearn

import math

# Training data
data = [
    [2, 4, 'A'],
    [4, 6, 'A'],
    [4, 4, 'A'],
    [4, 2, 'B'],
    [6, 4, 'B'],
    [6, 2, 'B']
]

# Test sample
test = [5, 3]

# Calculate distances
distances = []

for row in data:
    distance = math.sqrt((row[0] - test[0])**2 +
                         (row[1] - test[1])**2)
    distances.append((distance, row[2]))

# Sort distances
distances.sort()

# K = 3
k = 3
neighbors = distances[:k]

# Count classes
countA = 0
countB = 0

for n in neighbors:
    if n[1] == 'A':
        countA += 1
    else:
        countB += 1

# Prediction
if countA > countB:
    prediction = 'A'
else:
    prediction = 'B'

print("Test Sample:", test)
print("Predicted Class:", prediction)
