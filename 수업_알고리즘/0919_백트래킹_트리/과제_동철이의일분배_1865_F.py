import sys

sys.stdin = open("1865_input.txt", "r")


def max_v(row, value):
    global max_property

    if row == N:
        if max_property <= value:
            max_property = value
        return

    # 현재 값이 맥스보다 작으면
    # 곱해주는 값이 1보다 작으니까
    # 무조건 작을 수 밖에 없기 때문에
    # return
    if value <= max_property:
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

    print(f"#{tc} {max_property * 100:.6f}")
