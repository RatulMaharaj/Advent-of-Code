import pandas as pd

data = pd.read_csv("1_data.txt", names=["Data"])["Data"]


for i in data:
    for j in data:
        for k in data:
            if i == j == k:
                pass
            elif i + j + k == 2020:
                print(i, j, k)
                print(i + j + k)
                print(i * j * k)
