# Simple EM Algorithm Demonstration

data = [2, 4, 5, 10, 12, 14]

# Initial Means
mean1 = 3
mean2 = 12

print("Initial Means:")
print("Mean1 =", mean1)
print("Mean2 =", mean2)

# E-Step (Assign points to nearest mean)
cluster1 = []
cluster2 = []

for x in data:
    if abs(x - mean1) < abs(x - mean2):
        cluster1.append(x)
    else:
        cluster2.append(x)

# M-Step (Update means)
mean1 = sum(cluster1) / len(cluster1)
mean2 = sum(cluster2) / len(cluster2)

print("\nCluster 1:", cluster1)
print("Cluster 2:", cluster2)

print("\nUpdated Means:")
print("Mean1 =", round(mean1, 2))
print("Mean2 =", round(mean2, 2))
