import sys

sys.stdin = open("1226_input.txt", "r")

#    상  하  좌  우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N


def bfs(sr, sc):
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append((sr, sc))
    visited[sr][sc] = 1

    while q:
        r, c = q.pop(0)
        if miro[r][c] == 3:
            return 1

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if is_valid(nr, nc) and miro[nr][nc] != 1 and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = 1

    return 0


T = 10
for tc in range(1, T + 1):
    t = int(input())
    N = 16
    miro = [list(map(int, input())) for _ in range(N)]

    sr = sc = 0
    for r in range(N):
        for c in range(N):
            if miro[r][c] == 2:
                sr, sc = r, c

    answer = bfs(sr, sc)
    print(f"#{t} {answer}")
