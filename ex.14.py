# House Price Prediction using Linear Regression

x = [1000, 1500, 2000, 2500, 3000]
y = [2000000, 3000000, 4000000, 5000000, 6000000]

n = len(x)

sum_x = sum(x)
sum_y = sum(y)

sum_xy = sum([x[i] * y[i] for i in range(n)])
sum_x2 = sum([x[i] ** 2 for i in range(n)])

# Calculate slope
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)

# Calculate intercept
c = (sum_y - m * sum_x) / n

# Predict house price
area = int(input("Enter House Area (sq.ft): "))

price = m * area + c

print("Predicted House Price =", round(price, 2))
