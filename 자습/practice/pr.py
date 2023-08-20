import sys
sys.stdin = open("input.txt", "r")
#    상  하  좌  우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    balloon = [list(map(int, input().split())) for _ in range(N)]

    # 최대값
    max_sum = 0
    # 풍선 돌면서
    for r in range(N):
        for c in range(M):

            # 각 지점에서의 합
            flower_sum = balloon[r][c]
            # 상하좌우
            for k in range(4):
                # 터지는 풍선만큼 더
                for d in range(1, balloon[r][c] + 1):
                    nr = r + dr[k] * d
                    nc = c + dc[k] * d
                    # 범위안에 있으면
                    if 0 <= nr < N and 0 <= nc < M:
                        # 각 지점에서의 범위에 있는 상하좌우 합
                        flower_sum += balloon[nr][nc]

            # 최대값에 입력
            if max_sum < flower_sum:
                max_sum = flower_sum

    print(f"#{tc} {max_sum}")