import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    count = 0

    for r in range(N):
        for c in range(M):

            stack = []
            if arr[r][c] == 1:
                count += 1
                arr[r][c] = 0

                while True:
                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]

                        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 0:
                            stack.append((r, c))
                            arr[nr][nc] = 0
                            r, c = nr, nc
                            break
                    else:
                        if stack:
                            r, c = stack.pop()
                        else:
                            break

    print(count)
