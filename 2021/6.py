# Advent of Code 2021
# Day 6

# Solution to part one

f = open("./6_data.txt", "r")
initial_state = [int(item) for item in f.readlines()[0].split(",")]
f.close()


updated_state = [item for item in initial_state]
children = {f"{i}": 0 for i in range(0, 9)}


def handle_growth(state):
    for i in range(len(state)):
        if state[i] == 0:
            state[i] = 6
            children["8"] += 1
        else:
            state[i] -= 1

    return state


def handle_child_growth(children):
    create_new = children["0"]

    for i in range(1, 9):
        children[f"{i-1}"] = children[f"{i}"]

    children["8"] = 0
    children["8"] += create_new
    children["6"] += create_new


days_to_wait = 256


for day in range(1, days_to_wait + 1):
    handle_child_growth(children)
    updated_state = handle_growth(updated_state)

print(
    f"After {days_to_wait} days, there are {len(updated_state) + sum(children.values()) } lanternfish."
)
