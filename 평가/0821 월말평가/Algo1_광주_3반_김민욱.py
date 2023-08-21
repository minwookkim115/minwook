import sys
sys.stdin = open("algo1_sample_in.txt")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    balloon = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0  # 최대값
    min_v = 10000  # 최소값

    # 풍선을 돌면서
    for r in range(N):
        for c in range(N):

            # 풍선을 터트렸을 때 점수
            bomb = balloon[r][c]
            # 상하좌우 돌면서
            for k in range(4):
                # 그 자리의 수만큼 터트림
                for d in range(1, balloon[r][c] + 1):
                    nr = r + dr[k] * d
                    nc = c + dc[k] * d
                    # 범위안에 있을 때
                    if 0 <= nr < N and 0 <= nc < N:
                        # 점수 더하기
                        bomb += balloon[nr][nc]
            # 최대값에 넣고
            if max_v <= bomb:
                max_v = bomb
            # 최소값에 넣고
            if min_v >= bomb:
                min_v = bomb

    print(f"#{tc} {max_v - min_v}")
