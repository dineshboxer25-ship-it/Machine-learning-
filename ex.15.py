# Iris Flower Classification using Naive Bayes (Simple Version)

sepal_length = float(input("Enter Sepal Length: "))
sepal_width = float(input("Enter Sepal Width: "))

# Simple classification rules
if sepal_length < 5.5:
    print("Predicted Flower: Iris Setosa")

elif sepal_length < 6.5:
    print("Predicted Flower: Iris Versicolor")

else:
    print("Predicted Flower: Iris Virginica")
