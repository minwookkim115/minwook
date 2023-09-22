import sys

sys.stdin = open("2105_input.txt", "r")

dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]


def find(r, c, a, check1):
    global count

    if r == i + 1 and c == j - 1:
        if count >= len(check1):
            count = len(check1)
        return

    if tour[r][c] not in check1:
        check1.append(tour[r][c])
    else:
        return


    for k in range(4):
        if k >= a:
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                find(nr, nc, k, check1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tour = [list(map(int, input().split())) for _ in range(N)]
    count = -1

    for i in range(N - 2):
        for j in range(1, N - 1):
            find(i, j, -1, [])

    print(f"#{tc} {count}")
