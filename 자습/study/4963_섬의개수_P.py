import sys
sys.setrecursionlimit(1000000)

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def dfs(r, c):
    sea[r][c] = 0

    for k in range(8):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < H and 0 <= nc < W and sea[nr][nc] == 1:
            dfs(nr, nc)


while True:
    W, H = map(int, input().split())
    sea = [list(map(int, input().split())) for _ in range(H)]

    if W == 0 and H == 0:
        break

    answer = 0

    for r in range(H):
        for c in range(W):
            if sea[r][c] == 1:
                dfs(r, c)
                answer += 1

    print(answer)