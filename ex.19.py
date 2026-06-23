from sklearn.naive_bayes import GaussianNB

X = [[50000], [60000], [70000], [80000]]
y = [0, 1, 1, 1]

model = GaussianNB()
model.fit(X, y)

result = model.predict([[65000]])

if result[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")
