import pandas as pd
from sklearn.model_selection import train_test_split
import sklearn.linear_model as linear_model
import matplotlib.pyplot as plt

train = pd.read_csv("data/cinema.csv")
print(train.head())

print("checking missing values")
print(train.isnull().any(axis=0))

train = train.fillna(train.mean())
print(train.isna().any(axis=0))

print("filling n/a finished")

print("dropping outliers")
outliers= train[(train["SNS2"] > 1000) & (train["sales"] < 8500)]
train = train.drop(outliers.index, axis=0)
print("dropped outliers successfully")

train.plot(kind="scatter", x="SNS2", y="sales")
plt.show()

xcol = ["SNS1", "SNS2", "actor", "original"]
x = train[xcol]

ycol = ["sales"]
y = train[ycol]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
model = linear_model.LinearRegression()
model.fit(x_train, y_train)

print(model.coef_)

score = model.score(x_test, y_test)
print(score)