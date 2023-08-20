T = 10

# d = 0 아래
# d = 1 왼쪽
# d = 2 오른쪽
dr = [1, 0, 0]
dc = [0, -1, 1]

for tc in range(1, T + 1):
    tc = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]

    ladder_rev = []

    for i in range(99, 0, -1):
        ladder_rev.append(ladder[i])

    d = 0

    r = 0
    c = ladder_rev[0].index(2)

    nr = 0
    nc = 0

    while r > 0:

        nr = r + dr[d]
        nc = c + dc[d]

        if ladder_rev[nr][nc - 1] == 1:
            while ladder_rev[nr][nc] == 0:
                d = 1
                nr = r + dr[d]
                nc = c + dc[d]


        elif ladder_rev[nr][nc + 1] == 1:
            while ladder_rev[nr][nc] == 0:
                d = 2
                nr = r + dr[d]
                nc = c + dc[d]
