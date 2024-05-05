import pandas as pd
pd.options.display.max_columns = None

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def main():
  raw = pd.read_csv("data/Boston.csv")
  save_price_scatter(raw, x="CRIME")

  dummies = set_dummies(raw)
  
  # save_all_scatter_price_explanatory_variables(dummies)
  
  train, test = train_test_split(dummies, test_size=0.2, random_state=0)
  
  train = fill_missing_values(train)
  
  train = remove_outliers(train)
  x, y = get_x_y(train)
    
  model = learn(x, y)
  
  x_test, y_test = get_x_y(test)
  score_test = model.score(
    X=standardize(x_test), 
    y=standardize(y_test)
  )
  print(f"test score: {score_test}")
  
  print("RM", "PTRATIO", "LSTAT", "RM2", "RM*LSTAT")
  print(model.coef_)
  
def set_dummies(df: pd.DataFrame) -> pd.DataFrame:
  crime_dummies = pd.get_dummies(df["CRIME"], drop_first=True)
  # Rename columns
  crime_dummies.columns = ["LOW_CRIME_RATE", "VERY_LOW_CRIME_RATE"]
  
  df = pd.concat([df, crime_dummies], axis=1).drop("CRIME", axis=1)
  
  return df
  
def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
  df["NOX"] = df["NOX"].fillna(df["NOX"].mean())
  df["RAD"] = df["RAD"].fillna(df["RAD"].mean())
  return df

def remove_outliers(df: pd.DataFrame) -> pd.DataFrame:
  outlier_criteria = ((df["RM"] > 4.0) & (df["RM"] <= 5.0) & (df["PRICE"] >= 49) & (df["PRICE"] <= 51))
  df_filtered = df[~outlier_criteria]
  return df_filtered

def standardize(df :pd.DataFrame) -> pd.array:
  ss = StandardScaler()
  ss.fit(df)
  
  return ss.transform(df)

def get_x_y(df: pd.DataFrame):
    df["RM2"] = df["RM"] ** 2
    df["RM*LSTAT"] = df["RM"]*df["LSTAT"]
    
    xcol = ["RM", "PTRATIO", "LSTAT", "RM2", "RM*LSTAT"]
    x = df[xcol]
    y = df[["PRICE"]]
    
    return x, y

def learn(x: pd.DataFrame, y: pd.DataFrame) -> LinearRegression:
  x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=0)
  
  s_x = standardize(x_train)
  s_y = standardize(y_train)
  
  model = LinearRegression()
  model.fit(s_x, s_y)
  
  train_score = model.score(s_x, s_y)
  val_score = model.score(
    X=standardize(x_val), 
    y=standardize(y_val)
  )
  
  print(f"train_score: {train_score}, val_score: {val_score}")
  
  return model
  
def save_all_scatter_price_explanatory_variables(df: pd.DataFrame):
  save_price_scatter(df, x="ZN")
  save_price_scatter(df, x="INDUS")
  save_price_scatter(df, x="CHAS")
  save_price_scatter(df, x="NOX")
  save_price_scatter(df, x="RM")
  save_price_scatter(df, x="AGE")
  save_price_scatter(df, x="DIS")
  save_price_scatter(df, x="RAD")
  save_price_scatter(df, x="TAX")
  save_price_scatter(df, x="PTRATIO")
  save_price_scatter(df, x="B")
  save_price_scatter(df, x="LSTAT")

def save_price_scatter(df: pd.DataFrame, x: str):
  df.plot(kind="scatter", x=x, y="PRICE")
  save_path = f"fig/{x}.png"
  plt.savefig(save_path)

def plot_price_scatter(df: pd.DataFrame, x: str):
  df.plot(kind="scatter", x=x, y="PRICE")
  plt.show()

if __name__ == "__main__":
    main()