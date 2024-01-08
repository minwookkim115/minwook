from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

dr = [-1, 0, 0, 1]
dc = [0, 1, -1, 0]


def find(r, c):
    queue = deque()
    queue.append((r, c))

    while queue:
        r, c = queue.popleft()

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == 1:
                queue.append((nr, nc))
                maze[nr][nc] = maze[r][c] + 1

    return maze[N - 1][M - 1]


print(find(0, 0))
