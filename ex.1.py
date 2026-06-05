# Find-S Algorithm

def find_s(concepts, target):
    specific_h = concepts[0].copy()

    for i, h in enumerate(concepts):
        if target[i] == "Yes":  # Consider only positive examples
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'

    return specific_h


# Training Data
concepts = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change']
]

target = ['Yes', 'Yes', 'No', 'Yes']

# Apply Find-S
hypothesis = find_s(concepts, target)

print("Most Specific Hypothesis:")
print(hypothesis)
