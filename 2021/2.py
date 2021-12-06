# Advent of Code 2021
# Day 2

# Solution to part one

horizontal = 0
depth = 0

with open("./2_data.txt", "r") as f:
    for line in f:
        action, unit = line.split()
        if action == "forward":
            horizontal += int(unit)
        elif action == "up":
            depth -= int(unit)
        elif action == "down":
            depth += int(unit)

print(horizontal * depth)

# Solution to part two

horizontal = 0
depth = 0
aim = 0

with open("./2_data.txt", "r") as f:
    for line in f:
        action, unit = line.split()
        if action == "forward":
            horizontal += int(unit)
            depth += aim * int(unit)
        elif action == "up":
            aim -= int(unit)
        elif action == "down":
            aim += int(unit)

print(horizontal * depth)
