import sys
sys.stdin = open("1861_input.txt", "r")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    print(room)

    start = 0
    max_v = 0

    for r in range(N):
        count = 1
        for c in range(N):

            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]

                if 0 <= nr < N and 0 <= nc < N and room[r][c] + 1 == room[nr][nc]:
                    count += 1
                    r, c = nr, nc

        if max_v <= count:
            max_v = count


    print(start, max_v)