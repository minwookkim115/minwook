import sys
sys.stdin = open("과제_input.txt", "r")

T= 10

for tc in range(1, T + 1):
    N = int(input())
    str_board = [list(map(str, input())) for _ in range(8)]

    for r in range(8 - N + 1):
        for c in range(8 - N + 1):

            str_list = []
            for nr in range(r, r + N):
                for nc in range(c, c + N):
                    str_list.append(str_board[nr][nc])