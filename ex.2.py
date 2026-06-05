import csv

# Read CSV file
data = []

with open('trainingdata.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    for row in reader:
        data.append(row)

# Number of attributes
num_attr = len(data[0]) - 1

# Initialize S and G
S = ['0'] * num_attr
G = [['?'] * num_attr]

print("Initial Specific Hypothesis:")
print(S)

print("\nInitial General Hypothesis:")
print(G)

for row in data:
    attributes = row[:-1]
    target = row[-1]

    if target == "Yes":

        # Update S
        if S == ['0'] * num_attr:
            S = attributes.copy()

        for i in range(num_attr):
            if S[i] != attributes[i]:
                S[i] = '?'

        # Remove inconsistent hypotheses from G
        G = [g for g in G if all(
            g[i] == '?' or g[i] == attributes[i]
            for i in range(num_attr)
        )]

    else:  # Negative Example

        G_new = []

        for g in G:
            for i in range(num_attr):

                if g[i] == '?':
                    if S[i] != attributes[i]:
                        new_g = g.copy()
                        new_g[i] = S[i]
                        G_new.append(new_g)

        G = G_new

    print("\nCurrent S:")
    print(S)

    print("Current G:")
    print(G)

print("\nFinal Specific Hypothesis (S):")
print(S)

print("\nFinal General Hypotheses (G):")
for g in G:
    print(g)
