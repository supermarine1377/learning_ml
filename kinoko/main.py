import pandas as pd
import sklearn.tree as tree

train = pd.read_csv("data/train.csv")
print(train.head())

x = ["height", "weight", "age"]
y = ["like"]

X = train[x]
Y = train[y]

model = tree.DecisionTreeClassifier(random_state=0)
model.fit(X, Y)

test = pd.read_csv("data/test.csv")
x_test=test[x]
p = model.predict(x_test)
for pp in p:
  print(pp)
  
print(f"score: {model.score(X, Y)}")
