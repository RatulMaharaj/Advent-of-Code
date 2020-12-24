import pandas as pd

df = pd.read_csv("3_data.txt", names=["map"])

rows = 323  # the number of rows in the provided data
cols = 7 * rows + 1  # calculate the number of columns needed since the pattern repeats
multiple = cols / 31 + 1

df["extended map"] = df["map"].map(lambda x: x * int(multiple))


def traverse(right, down):
    column = 0
    count = 0
    for row, value in enumerate(df["extended map"]):
        if down > 1:
            if row % down == 0:
                continue
        try:
            column += right
            # print(row + 1, column)
            if df["extended map"][row + 1][column] == "#":
                count += 1

        except:
            pass
    return count


# print(traverse(1, 1))
# print(traverse(3, 1))
# print(traverse(5, 1))
# print(traverse(7, 1))
# print(traverse(1, 2))

answer = (
    traverse(1, 1) * traverse(3, 1) * traverse(5, 1) * traverse(7, 1) * traverse(1, 2)
)

print(answer)
