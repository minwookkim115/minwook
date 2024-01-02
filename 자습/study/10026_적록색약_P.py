import sys
sys.setrecursionlimit(10**6)

N = int(input())
color = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
answer1 = 0
answer2 = 0


def area(r, c):
    visited[r][c] = 1
    check = color[r][c]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if visited[nr][nc] == 0:
                if color[nr][nc] == check:
                    area(nr, nc)


for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            area(i, j)
            answer1 += 1

for i in range(N):
    for j in range(N):
        if color[i][j] == 'G':
            color[i][j] = 'R'

visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            area(i, j)
            answer2 += 1

print(answer1, answer2)