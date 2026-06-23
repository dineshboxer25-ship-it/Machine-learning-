# Compare Classification Algorithms

algorithms = ["KNN", "Naive Bayes", "Decision Tree", "Perceptron"]

accuracy = [90, 85, 95, 88]

print("Algorithm\tAccuracy (%)")
print("--------------------------")

for i in range(len(algorithms)):
    print(algorithms[i], "\t\t", accuracy[i])

best = max(accuracy)
index = accuracy.index(best)

print("\nBest Algorithm =", algorithms[index])
print("Highest Accuracy =", best, "%")
