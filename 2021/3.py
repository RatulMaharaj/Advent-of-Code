# Advent of Code 2021
# Day 3

# Solution to part one
import pandas as pd

df = pd.DataFrame({f"{key}": [] for key in range(1, 13)})

with open("3_data.txt", "r") as f:
    for line in f:
        df.loc[df.shape[0]] = [item for item in list(line) if item != "\n"]

gamma = ""
epislon = ""

for i in range(1, 13):
    gamma += str(df[f"{i}"].value_counts().idxmax())
    epislon += str(df[f"{i}"].value_counts().idxmin())


print("Solution to part one:", int(gamma, 2) * int(epislon, 2), "\n")

# Solution to part two

# O2 Rating
tmp = df.copy(deep=True)
tmp["keep"] = True


for i in range(1, 13):
    if tmp.shape[0] == 1:
        break
    elif len(tmp[f"{i}"].mode()) > 1:
        tmp["keep"] = tmp[f"{i}"].map(lambda x: True if x == "1" else False)
    else:
        keep_value = tmp[f"{i}"].mode()[0]
        tmp["keep"] = tmp[f"{i}"].map(lambda x: True if x == keep_value else False)

    tmp = tmp[tmp["keep"]]

O2_rating = "".join(list(tmp.reset_index().iloc[0, 1:-1]))

# CO2 Rating

tmp = df.copy(deep=True)
tmp["keep"] = True

for i in range(1, 13):
    if tmp.shape[0] == 1:
        break
    elif len(tmp[f"{i}"].mode()) > 1:
        tmp["keep"] = tmp[f"{i}"].map(lambda x: True if int(x) == 0 else False)
    else:
        keep_value = int(tmp[f"{i}"].mode()[0])

        if keep_value == 1:
            keep_value = 0
        elif keep_value == 0:
            keep_value = 1

        tmp["keep"] = tmp[f"{i}"].map(lambda x: True if int(x) == keep_value else False)

    tmp = tmp[tmp["keep"]]


CO2_rating = "".join(list(tmp.reset_index().iloc[0, 1:-1]))

life_support_rating = int(O2_rating, 2) * int(CO2_rating, 2)
print("Solution to part two: ", life_support_rating)
