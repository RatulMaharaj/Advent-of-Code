# Advent of Code 2021
# Day 4

# Solution to part one
import copy


numbers = []
boards = []

with open("./4_data.txt", "r") as f:
    boards_count = 0
    board = []
    for pos, line in enumerate(f):
        if pos == 0:
            numbers = [int(item) for item in line.split(",")]
        else:
            if line == "\n":
                if pos != 1:
                    boards.append(board)
                    board = []
            else:
                board.append([int(item) for item in line.split()])
    boards.append(board)

boards_b = copy.deepcopy(boards)


def calculate_sum(board):
    total = 0
    for row in board:
        for item in row:
            if item != "X":
                total += item
    return total


def check_rows(board):
    for row in board:
        if row == ["X" for i in range(0, 5)]:  # if we have row bingo
            return True
    else:
        return False


def check_cols(board):
    transposed_board = []
    for i in range(0, 5):
        new_row = []
        for j in range(0, 5):
            new_row.append(board[j][i])
        transposed_board.append(new_row)
    return check_rows(transposed_board)


def check_for_bingo(board):
    if check_cols(board) or check_rows(board):
        return True
    else:
        return False


def mark_board(board, number):
    for i in range(0, 5):
        for j in range(0, 5):
            if board[i][j] == number:
                board[i][j] = "X"


for number in numbers:
    print("Calling number: ", number)
    got_bingo = False
    for board in boards:
        mark_board(board, number)
        bingo = check_for_bingo(board)
        if bingo:
            got_bingo = True
            print("The last number called was: ", number)
            print("The sum of the remaining numbers are:", calculate_sum(board))
            print("The score is: ", number * calculate_sum(board))
            print("\n")
            break
    if got_bingo:
        break


# Solution to part two


for number in numbers:
    print("Calling number: ", number)
    for board in boards_b:
        already_found = check_for_bingo(board)
        if already_found:
            continue
        else:
            mark_board(board, number)
            bingo = check_for_bingo(board)
            if bingo:
                print("Found a bingo!")
                print("The last number called was: ", number)
                print("The sum of the remaining numbers are:", calculate_sum(board))
                print("The score is: ", number * calculate_sum(board))
