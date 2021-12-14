# Advent of Code 2021
# Day 5

# Solution to part one

import pandas as pd

path = "./5_data.txt"

data = []

with open(file=path) as f:
    raw_data = f.readlines()
    for item in raw_data:
        x1, y1, x2, y2 = [int(el) for el in item.replace("->", ",").split(",")]
        data.append({"x1": x1, "y1": y1, "x2": x2, "y2": y2})

df = pd.DataFrame(data)

min_x, min_y = 0, 0
max_x = max(df.max()["x1"], df.max()["x2"])
max_y = max(df.max()["y1"], df.max()["y2"])

grid = [(max_x + 1) * ["."] for y in range(min_y, max_y + 1)]


def display_grid():
    for row in grid:
        print(" ".join(row))
    print("\n")


def update_grid(x, y):
    if grid[y][x] == ".":
        grid[y][x] = "1"
    else:
        grid[y][x] = str(int(grid[y][x]) + 1)


for item in data:
    if item["x1"] == item["x2"]:
        # update the grid with a vertical line
        if item["y2"] > item["y1"]:
            for i in range(item["y1"], item["y2"] + 1):
                update_grid(item["x1"], i)
        else:
            for i in range(item["y2"], item["y1"] + 1):
                update_grid(item["x1"], i)

    elif item["y1"] == item["y2"]:
        # update the grid with a horizontal line
        if item["x2"] > item["x1"]:
            for i in range(item["x1"], item["x2"] + 1):
                update_grid(i, item["y1"])
        else:
            for i in range(item["x2"], item["x1"] + 1):
                update_grid(i, item["y1"])

display_grid()


def count_overlaps():
    overlaps = 0
    for row in grid:
        for item in row:
            if item != ".":
                if int(item) >= 2:
                    overlaps += 1

    return overlaps


print(count_overlaps(), "overlaps occur")
