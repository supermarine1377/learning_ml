import pandas as pd
from sklearn.preprocessing import StandardScaler
pd.options.display.max_columns = None

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import numpy as np

import matplotlib.pyplot as plt

def main():
  raw = pd.read_csv("data/tips.csv")
  processed = set_dummies(raw)
  
  train, test = train_test_split(
    processed, 
    test_size=0.3,
    random_state=0,
  )
  
  train_x, train_y = get_x_y(train)
  sx_model = StandardScaler()
  sx_model.fit(train_x)
  sy_model = StandardScaler()
  sy_model.fit(train_y)
  
  train_x_2, val_x, train_y_2, val_y = train_test_split(
    train_x, 
    train_y, 
    test_size=0.3, 
    random_state=0,
  )
  
  model = learn(
    sx_model.transform(train_x_2), 
    sy_model.transform(train_y_2),
  )
  
  train_score = model.score(
    sx_model.transform(train_x_2),
    sy_model.transform(train_y_2)
  )
  print(f"train_score: {train_score}")
  
  val_score = model.score(
    sx_model.transform(val_x),
    sy_model.transform(val_y)
  )
  print(f"val_score: {val_score}")
  
  test_x, test_y = get_x_y(test)
  test_score =model.score(
    sx_model.transform(test_x),
    sy_model.transform(test_y),
  )
  print(f"test score: {test_score}")
  
  coef = pd.DataFrame(model.coef_)
  coef.columns = train_x.columns
  print(coef)
  print(f"intercept: {model.intercept_}")

  # print(test_x)
  p = model.predict(test_x)
  print(p)
  p = np.insert(p, 0, 0)
  p_reversed = reverse_standardize(p, sy_model)
  # print(p_reversed.shape)
  # print(test_x.shape)
  pdf = pd.DataFrame(data=p_reversed)
  pdf = pd.concat(objs=[test_x, pdf], axis=1)
  # print(pdf)
  predicted = pd.concat(objs=[test_x, pdf], axis=1)
  # print(predicted.shape)
    
def set_dummies(df: pd.DataFrame) -> pd.DataFrame:
  sex = pd.get_dummies(
    data=df["sex"], 
    drop_first=True
  )
  sex = sex.rename(columns={"Male": "is_billpayer_male"})
  
  smoker = pd.get_dummies(
    data=df["smoker"],
    drop_first=True
  )
  smoker = smoker.rename(columns={"Yes": "has_smoker"})

  day = pd.get_dummies(
    data=df["day"],
    drop_first=False
  )
  day = day.rename(
    columns={
      "Sat": "is_sat", 
      "Sun": "is_sun", 
      "Thur": "is_thur",
      "Fri": "is_fri",
    }
  )
  
  time = pd.get_dummies(
    data=df["time"],
    drop_first=True
  )
  time = time.rename(columns={"Lunch": "is_lunch"})
  
  df = pd.concat(objs=[df, sex, smoker, day, time], axis=1)
  df = df.drop("sex", axis=1)
  df = df.drop("smoker", axis=1)
  df = df.drop("day", axis=1)
  df = df.drop("time", axis=1)
  
  return df

def reverse_standardize(predicted: np.ndarray, ss: StandardScaler):
  return ss.inverse_transform(predicted.reshape(-1, 1))

def get_x_y(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
  df["tip_percentage"] = df["tip"] / df["total_bill"]
  
  xcol = [
    "total_bill", 
    "tip_percentage",
    # "total_bill*total_bill*size",
    # "size", 
    # "is_billpayer_male",
    # "has_smoker",
    # "is_sat",
    # "is_sun", 
    # "is_thur",
    # "is_lunch",
  ]
  x = df[xcol]
  y = df[["tip"]]
    
  return x, y

def learn(x_train: pd.DataFrame, y_train: pd.DataFrame) -> LinearRegression:
  model = LinearRegression()
  model.fit(x_train, y_train)

  return model

def save_all_tip_scatter(df: pd.DataFrame):
  temp = df  
  save_tip_scatter(temp, "total_bill")
  save_tip_scatter(temp, "size")
  
  # boolのままで散布図を書こうとするとエラーになってしまうので数値に変換している
  # raise KeyError(key) from err KeyError: 'is_billpayer_male'
  temp["is_billpayer_male"] = temp["is_billpayer_male"].astype(int) 
  save_tip_scatter(temp, "is_billpayer_male")
  
  temp["has_smoker"] = temp["has_smoker"].astype(int)
  save_tip_scatter(temp, "has_smoker")
  
  temp["is_sat"] = temp["is_sat"].astype(int)
  save_tip_scatter(temp, "is_sat")

  temp["is_sun"] = temp["is_sun"].astype(int)
  save_tip_scatter(temp, "is_sun")

  temp["is_thur"] = temp["is_thur"].astype(int)
  save_tip_scatter(temp, "is_thur")
 
  temp["is_fri"] = temp["is_fri"].astype(int)
  save_tip_scatter(temp, "is_fri")
  
  temp["is_lunch"] = temp["is_lunch"].astype(int)
  save_tip_scatter(temp, "is_lunch")

def save_tip_scatter(df: pd.DataFrame, x: str):
  df.plot(kind="scatter", x=x, y="tip")
  save_path = f"fig/{x}.png"
  plt.savefig(save_path)
  
def convert_to_int(df: pd.DataFrame, key: str) -> pd.DataFrame:
  df[str] = df[str].astype(int)
  return df

def save_scatter_total_bill_size(df: pd.DataFrame):
  temp = df
  temp.plot(kind="scatter", x="total_bill", y="size")
  save_path = "fig/total_bill_vs_size"
  plt.savefig(save_path)
  
  # print(temp.corr()["total_bill"])
  
def plot_residual(test_x_y: pd.DataFrame, model: LinearRegression):
  test_x, test_y = get_x_y(test_x_y)

  
if __name__ == "__main__":
  main()