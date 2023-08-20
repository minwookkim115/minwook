import sys

sys.stdin = open("1974_input.txt", "r")


def sudoku(arr):
    for r in range(9):
        count = [0] * 10
        for c in range(9):
            count[arr[r][c]] += 1
        # print(count)
        for i in range(1, 10):
            if count[i] == 0:
                return 0

    for r in range(9):
        count = [0] * 10
        for c in range(9):
            count[arr[c][r]] += 1
        # print(count)
        for i in range(1, 10):
            if count[i] == 0:
                return 0

    for r in range(0, 6, 3):
        for c in range(0, 6, 3):
            count = [0] * 10
            for nr in range(0, 3):
                for nc in range(0, 3):
                    count[arr[r + nr][c + nc]] += 1
            for i in range(1, 10):
                if count[i] == 0:
                    return 0
    return 1


T = int(input())

for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    answer = sudoku(arr)
    print(f"#{tc} {answer}")
