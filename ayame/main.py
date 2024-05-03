import pandas as pd
from sklearn.model_selection import train_test_split
import sklearn.tree as tree
import matplotlib.pyplot as plt

train = pd.read_csv("data/iris.csv")
print("head")
print(train.head())

print("species")
print(train["species"].unique())
print(train["species"].value_counts())

print("missing value")
print(train.isna().any(axis=0))

xcol = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
x = train[xcol].fillna(train[xcol].mean())
print(x.isna().any(axis=0))

ycol = ["species"]
y = train[ycol]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.35, random_state=0)
model = tree.DecisionTreeClassifier(random_state=0)

model.fit(x_train, y_train)
score = model.score(x_test, y_test)

print(score)

plt.figure(figsize=(15, 10))
tree.plot_tree(model, feature_names=xcol, filled=True)
plt.show()

