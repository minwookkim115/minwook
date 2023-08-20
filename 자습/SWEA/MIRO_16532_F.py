import sys

sys.stdin = open("16532_input.txt", "r")


def find_road(r, c, n, miro):
    #    상  하  좌  우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    stack = []
    visited = [[0] * n for _ in range(n)]
    visited[r][c] = 1  # 출발점 방문 1

    while True:
        if miro[r][c] == 3:  # 3이면 도착지
            return 1
        # 상하좌우 돌면서
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            # 범위안에 있고, 1이 아니고, 방문안했으면
            if 0 <= nr < N and 0 <= nc < N and miro[nr][nc] != 1 and visited[nr][nc] == 0:
                stack.append((r, c))  # 돌아갈 곳 append
                visited[nr][nc] = 1  # 방문했으니까 1
                r, c = nr, nc  # 진행방향
                break
        # 갈곳 없으면
        else:
            if stack:  # 스택에 돌아갈곳이 있으면
                r, c = stack.pop()  # pop해서 돌아가기
            else:
                return 0  # 갈곳 없으면 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 미로 범위
    arr = [list(map(int, input())) for _ in range(N)]  # 미로

    sr = 0  # 출발 행좌표
    sc = 0  # 출발 열좌표

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:  # 출발점 2가 있는곳의
                sr = r  # 행좌표
                sc = c  # 열좌표

    print(f"#{tc} {find_road(sr, sc, N, arr)}")
