# This solution is incomplete
import pandas as pd

df = pd.read_csv("5_data.txt", names=["Data"])

code = "FFBBFFFLRL"

rows = [row for row in range(0, 128)]


def reduce(rows, letter):
    if letter == "F":
        end = len(rows) // 2
        return rows[0:end]
    elif letter == "B":
        start = len(rows) // 2
        end = len(rows)
        return rows[start:end]


print(reduce(rows, "B"))