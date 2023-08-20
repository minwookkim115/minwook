import sys

sys.stdin = open("고대유적_input1.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ruins = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    for r in range(N):
        row_len = 0
        for c in range(M):
            if ruins[r][c] == 1:
                row_len += 1
                answer = max(row_len, answer)
            else:
                row_len = 0

    for c in range(M):
        col_len = 0
        for r in range(N):
            if ruins[r][c] == 1:
                col_len += 1
                answer = max(col_len, answer)
            else:
                col_len = 0

    print(f"#{tc} {answer}")