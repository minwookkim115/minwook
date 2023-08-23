import sys
sys.stdin = open("16268_input.txt", "r")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_pang = 0

    for r in range(N):
        for c in range(M):

            pang = arr[r][c]
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < M:
                    pang += arr[nr][nc]

            if max_pang < pang:
                max_pang = pang

    print(f"#{tc} {max_pang}")