T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flower_powder = [list(map(int, input().split())) for _ in range(N)]

    max_flower_powder = 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for r in range(N):
        for c in range(M):

            sum_flower_powder = flower_powder[r][c]

            pop_num = flower_powder[r][c]

            for d in range(4):

                for k in range(1, pop_num + 1):

                    nr = r + dr[d] * k
                    nc = c + dc[d] * k

                    if 0 <= nr < N and 0 <= nc < M:
                        sum_flower_powder += flower_powder[nr][nc]

            if max_flower_powder < sum_flower_powder:
                max_flower_powder = sum_flower_powder

    print(f"#{tc} {max_flower_powder}")
