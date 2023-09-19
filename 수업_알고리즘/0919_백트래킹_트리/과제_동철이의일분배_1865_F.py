import sys

sys.stdin = open("1865_input.txt", "r")


def max_v(row, value):
    global max_property

    if row == N:
        if max_property <= value:
            max_property = value
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            max_v(row + 1, value * (success[row][i] / 100))
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    success = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_property = 0
    max_v(0, 1)

    print(f"#{tc} {max_property * 100}")
