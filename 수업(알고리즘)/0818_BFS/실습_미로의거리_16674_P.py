import sys

sys.stdin = open("16674_input.txt", "r")

#    상  하  좌  우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 범위 안에있는지 판별하는 함수
def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N


# 미로찾기 함수
def bfs(sr, sc):
    visited = [[0] * N for _ in range(N)]

    # 큐생성, 출발점 append, 방문표시 1
    q = []
    q.append((sr, sc))
    visited[sr][sc] = 1

    while q:  # q가 빌때까지, 다 돌아볼 때 까지

        r, c = q.pop(0)  # 갈곳을 찾기위해 q에서 pop
        if miro[r][c] == 2:  # 도착하면
            return visited[r][c] - 2  # 출발점(-1)과 도착점(-1)을 제외한 -2의거리

        for k in range(4):  # 상하좌우
            nr = r + dr[k]
            nc = c + dc[k]
            # 범위안에 있고, 벽(1)이 아니고, 방문하지 않았으면
            if is_valid(nr, nc) and miro[nr][nc] != 1 and visited[nr][nc] == 0:
                q.append((nr, nc))  # q에 append
                visited[nr][nc] = visited[r][c] + 1  # 새로방문하는 곳에 전에 방문한 것에 +1해서 표시

    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]

    sr = sc = 0  # 출발 행, 열 좌표

    for r in range(N):
        for c in range(N):
            if miro[r][c] == 3:  # 3에서 출발
                sr, sc = r, c

    print(f"#{tc} {bfs(sr, sc)}")
