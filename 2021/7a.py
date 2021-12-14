# Advent of Code 2021
# Day 7

# Solution to part one

import numpy as np

with open("./7_data.txt", "r") as f:
    data = np.array([int(item.strip()) for item in f.readlines()[0].split(",")])

fuel_spend = {}

for x in range(0, max(data) + 1):
    fuel_spend[f"{x}"] = sum(abs(data - x))


print(
    f"Optimum Position: {list(fuel_spend.keys())[list(fuel_spend.values()).index(min(fuel_spend.values()))]} \nFuel spend: {min(fuel_spend.values())}"
)
