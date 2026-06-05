# Naive Bayes Classification

# Actual class labels
actual = ['Yes', 'No', 'Yes', 'Yes', 'No']

# Predicted class labels
predicted = ['Yes', 'No', 'Yes', 'No', 'No']

# Calculate confusion matrix values
TP = TN = FP = FN = 0

for i in range(len(actual)):
    if actual[i] == 'Yes' and predicted[i] == 'Yes':
        TP += 1
    elif actual[i] == 'No' and predicted[i] == 'No':
        TN += 1
    elif actual[i] == 'No' and predicted[i] == 'Yes':
        FP += 1
    elif actual[i] == 'Yes' and predicted[i] == 'No':
        FN += 1

# Display confusion matrix
print("Confusion Matrix")
print("----------------")
print("TP =", TP)
print("TN =", TN)
print("FP =", FP)
print("FN =", FN)

# Accuracy
accuracy = ((TP + TN) / len(actual)) * 100

print("\nAccuracy =", accuracy, "%")
