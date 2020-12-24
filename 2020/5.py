import pandas as pd

df = pd.read_csv("5_data.txt", names=["Data"])
print(df.head())