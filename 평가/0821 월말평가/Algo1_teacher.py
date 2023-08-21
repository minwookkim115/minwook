import sys
sys.stdin = open("algo1_sample_in.txt")

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    min_v = N * N * 10

    for r in range(N):
        for c in range(N):
            #(r, c) 에서 풍선을 터뜨렸을때 점수
            score = arr[r][c]

            for k in range(1, arr[r][c] + 1):
                for d in range(4):
                    nr = r + dr[d] * k
                    nc = c + dc[d] * k
                    if 0 <= nr < N and 0 <= nc < N:
                        score += arr[nr][nc]

            # 최대점수
            if max_v < score:
                max_v = score
            # 최소점수
            if min_v > score:
                min_v = score

    print(f"#{tc} {max_v - min_v}")
