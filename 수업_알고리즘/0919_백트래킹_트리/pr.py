import sys

sys.stdin = open("1865_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    success = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    max_property = 1
    count = 0

    while True:
        if count == N:
            break
        check = 0
        for r in range(N):
            for c in range(N):
                if visited[r][c] == 0 and success[r][c] >= check:
                    check = success[r][c]

        for r in range(N):
            for c in range(N):
                if success[r][c] == check:
                    max_property *= (success[r][c] / 100)
                    count += 1
                    for i in range(N):
                        visited[i][c] = 1
                        visited[r][i] = 1

    print(f"#{tc} {max_property * 100}")