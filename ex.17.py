from sklearn.linear_model import LinearRegression

X = [[4], [6], [8], [12]]
y = [15000, 20000, 25000, 35000]

model = LinearRegression()
model.fit(X, y)

price = model.predict([[10]])

print("Predicted Mobile Price:", price[0])
