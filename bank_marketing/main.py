import pandas as pd
pd.options.display.max_columns = None
from sklearn.model_selection import train_test_split
import sklearn.tree as tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

def main():
  raw = pd.read_csv("data/Bank.csv")
  
  filled = fill_missing_values(raw)
  all = set_dummies(filled)
  
  train_val, test = train_test_split(all, test_size=0.3, random_state=0)
  train, val = train_test_split(train_val, test_size=0.3, random_state=0)
  
  train_x, train_y = get_x_y(train)
  model = tree.DecisionTreeClassifier(max_depth=7, random_state=0)
  # model = RandomForestClassifier(n_estimators=300, random_state=0)
  model.fit(train_x, train_y)
  print(f"training score: {model.score(train_x, train_y)}")

  val_x, val_y = get_x_y(val)
  print(f"model validation score: {model.score(val_x, val_y)}")
  
  test_x, test_y = get_x_y(test)
  print(f"model test score: {model.score(test_x, test_y)}")
  
  plot_tree(
    decision_tree=model, 
    feature_names=train_x.columns, 
    precision=4,
    fontsize=6,
    filled=True,
  )
  plt.show()
  
  i = pd.Series(data=model.feature_importances_, index=train_x.columns)
  print(i)
  
def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
  is_duration_na = df["duration"].isna()
  df.loc[
    (df["y"] == 0)
    & (is_duration_na),
    "duration"
  ] = 301
  df.loc[
    (df['y'] == 1)
    & (is_duration_na),
    "duration"
  ] = 349
    
  return df

def set_dummies(df: pd.DataFrame) -> pd.DataFrame: 
  # drop columns which is unneeded
  df = df.drop("id", axis=1)
  df = df.drop("age", axis=1)
  df = df.drop("education", axis=1)
  df = df.drop("amount", axis=1)
  df = df.drop("day", axis=1)
  df = df.drop("month", axis=1)
  
  dummies_job = pd.get_dummies(df["job"], drop_first=True)
  df["is_student"] = dummies_job["student"]
  df = df.drop("job", axis=1)
  
  dummies_marital = pd.get_dummies(df["marital"], drop_first=True)
  # is_singleだけが特徴量として必要そうなので不要なカラムは削除する
  dummies_marital = dummies_marital.drop("married", axis=1)
  dummies_marital = dummies_marital.rename(
    columns= {
      "single": "is_single",
    }
  )
  df = df.drop("marital", axis=1)  

  dummies_loan = pd.get_dummies(df["loan"], drop_first=True)
  dummies_loan = dummies_loan.rename(
    columns={
      "yes": "has_loan",
    }
  )
  df = df.drop("loan", axis=1)
  
  dummies_housing = pd.get_dummies(df["housing"], drop_first=True)
  dummies_housing = dummies_housing.rename(
    columns={
      "yes": "has_housing_loan"
    }
  )
  df = df.drop("housing", axis=1)
  
  dummies_default = pd.get_dummies(df["default"], drop_first=True)
  dummies_default = dummies_default.rename(
    columns={
      "yes": "is_default"
    }
  )  
  df = df.drop("default", axis=1)
  
  dummies_contact = pd.get_dummies(df["contact"], drop_first=True)
  df["is_by_sending_document"] = dummies_contact["sending _document"]
  df = df.drop("contact", axis=1)
  
  df = pd.concat(
    objs=[
      df, 
      dummies_marital,
      dummies_loan,
      dummies_housing,
      dummies_default,
    ], 
    axis=1
  )

  return df

def get_x_y(df: pd.DataFrame):
  xcol = [
    "duration",
    "campaign",
    "previous",
    "is_student",
    "is_by_sending_document",
    "is_single",
    "has_loan",
    "has_housing_loan",
    "is_default",
  ]
  ycol = [
    "y"
  ]
  return df[xcol], df[ycol]

if __name__ == "__main__":
  main()