# Compare Linear and Polynomial Regression

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

print("Input Values")
for i in range(len(x)):
    print("X =", x[i], "Y =", y[i])

print("\nLinear Regression Prediction")
print("Linear model tries to fit a straight line.")

print("\nPolynomial Regression Prediction")
print("Polynomial model fits a curve.")

# Example prediction
x_new = 6

# Polynomial relation y = x^2
y_poly = x_new ** 2

print("\nPredicted value for X =", x_new)
print("Polynomial Regression Output =", y_poly)
