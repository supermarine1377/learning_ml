import pandas as pd
import sklearn.tree as tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

raw = pd.read_csv("data/Survived.csv")
print(raw.head())

train = raw

print("Convert Sex")
# train['Sex'] = train['Sex'].map({'male': 0, 'female': 1})
male = pd.get_dummies(train["Sex"], drop_first=True)

train = train.drop("Sex", axis=1)
train = pd.concat([train, male], axis=1)

print("Converted Sex successfully")

print("Convert Embarked")
train["Embarked"] = train["Embarked"].fillna(value=train["Embarked"].mode()[0])
embarked = pd.get_dummies(train["Embarked"], drop_first=True)
train = train.drop("Embarked", axis=1)
train = pd.concat([train, embarked], axis=1)

print(train.head())

print(
  pd.pivot_table(train, index='Survived', columns='Pclass', values='Age', aggfunc="mean")
)

print("Filling n/a ages")
is_age_na = train["Age"].isna()
train.loc[
  (train['Pclass'] == 1)
  & (train['Survived'] == 0)
  & (is_age_na), 
  'Age'
] = 43

train.loc[
  (train['Pclass'] == 2)
  & (train['Survived'] == 0)
  & (is_age_na), 
  'Age'
] = 33

train.loc[
  (train['Pclass'] == 3)
  & (train['Survived'] == 0)
  & (is_age_na), 
  'Age'
] = 26

train.loc[
  (train['Pclass'] == 1)
  & (train['Survived'] == 1)
  & (is_age_na), 
  'Age'
] = 35

train.loc[
  (train['Pclass'] == 2)
  & (train['Survived'] == 1)
  & (is_age_na), 
  'Age'
] = 25

train.loc[
  (train['Pclass'] == 3)
  & (train['Survived'] == 1)
  & (is_age_na), 
  'Age'
] = 20

print(train.isna().any(axis=0))

xcol = ["Pclass", "Age", "Fare", "male", "Q", "S"]
ycol = ["Survived"]
x = train[xcol]
y = train[ycol]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
model = tree.DecisionTreeClassifier(random_state=0, max_depth=10, class_weight="balanced")
model.fit(x_train, y_train)
score = model.score(x_test, y_test)
print(score)

df = pd.DataFrame(model.feature_importances_, index=xcol)
print(df)