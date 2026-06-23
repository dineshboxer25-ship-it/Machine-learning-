from sklearn.linear_model import LinearRegression

months = [[1], [2], [3], [4]]
sales = [1000, 1200, 1500, 1800]

model = LinearRegression()
model.fit(months, sales)

future = model.predict([[5]])

print("Predicted Sales:", future[0])
