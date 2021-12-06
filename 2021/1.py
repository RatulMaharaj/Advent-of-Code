# Advent of Code 2021
# Day 1

# Solution to part one
import pandas as pd

measurements = pd.read_csv("./1_data.txt", header=None)[0]


def count_increases(measurements: list):
    count = 0
    for pos, item in enumerate(measurements):
        if pos == 0:
            continue
        else:
            if (item - measurements[pos - 1]) > 0:
                count += 1
    return count


print(count_increases(measurements))

# Solution to part two

sums = []

for pos, item in enumerate(measurements):
    try:
        sums.append(item + measurements[pos + 1] + measurements[pos + 2])
    except:
        pass

print(count_increases(sums))
