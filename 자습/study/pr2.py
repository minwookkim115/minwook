dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

L, R, C = map(int, input().split())

buildings = []
visited = [[0] * R for _ in range(C)]

for i in range(L):
    building = [list(input()) for _ in range(R + 1)]
    buildings.append(building)

for i in buildings:
    i.pop()

sr = 0
sc = 0

er = 0
ec = 0

for i in buildings:
    for r in range(R):
        for c in range(C):
            if i[r][c] == "S":
                sr = r
                sc = c
            if i[r][c] == "E":
                er = r
                ec = c

count = 0
i = 0
visited[sr][sc] = 1
while i < L:
    for sr in range(R):
        for sc in range(C):

            for k in range(4):
                if buildings[i][sr][sc] == buildings[i + 1][sr][sc] == ".":
                    i += 1
                    break
                nr = sr + dr[k]
                nc = sc + dc[k]
                if 0 <= nr < R and 0 <= nc < C and buildings[i][nr][nc] != "#" and visited[nr][nc] != 1:
                    sr, sc = nr, nc
                    visited[nr][nc] = 1
                    count += 1