# import sys
# sys.setrecursionlimit(10000)
#
# N, M, K = map(int, input().split())
# coord = [list(map(int, input().split())) for _ in range(K)]
#
# paper = [[0] * M for _ in range(N)]
#
# for i in range(3):
#     for r in range(coord[i][1], coord[i][1] + coord[i][3] - coord[i][1]):
#         for c in range(coord[i][0], coord[i][0] + coord[i][2] - coord[i][0]):
#             paper[r][c] += 1
#
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
# visited = [[0] * M for _ in range(N)]
# answer = 0
# count = []
# sub_c = 1
#
#
# def find(r, c):
#     global count, answer, sub_c
#     visited[r][c] = 1
#
#     for k in range(4):
#         nr = r + dr[k]
#         nc = c + dc[k]
#         if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and paper[nr][nc] == 0:
#             sub_c += 1
#             find(nr, nc)
#
#
# for r in range(N):
#     for c in range(M):
#         if paper[r][c] == 0 and visited[r][c] == 0:
#             find(r, c)
#             answer += 1
#             count.append(sub_c)
#             sub_c = 1
#
# print(answer)
# count.sort()
# print(*count)

from collections import deque

N, M, K = map(int, input().split())
paper = [[0] * M for _ in range(N)]

for _ in range(K):
    r1, c1, r2, c2 = map(int, input().split())
    for r in range(c1, c2):
        for c in range(r1, r2):
            paper[r][c] += 1

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def find(r, c):
    queue = deque()
    queue.append((r, c))

    count = 1
    while queue:
        r, c = queue.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and paper[nr][nc] == 0:
                paper[nr][nc] = 1
                queue.append((nr, nc))
                count += 1

    return count

answer = []

for r in range(N):
    for c in range(M):
        if paper[r][c] == 0:
            paper[r][c] += 1
            answer.append(find(r, c))

print(len(answer))
answer.sort()
print(*answer)