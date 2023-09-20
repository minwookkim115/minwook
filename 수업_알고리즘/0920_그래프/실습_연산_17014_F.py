import sys

sys.stdin = open("17014_input.txt", "r")

cal = [1, -1, 2, -10]


def calculate(x, cnt):
    global min_cnt

    if x == M:
        min_cnt = cnt
        return

    if x <= 1 or x >= 1000000:
        return

    if cnt >= min_cnt:
        return

    for i in range(4):
        if i == 2:
            if x * cal[i] <= 1000000 and visited[x * cal[i]] == 0 and x * cal[i] <= M:
                visited[x * cal[i]] = 1
                calculate(x * cal[i], cnt + 1)
                visited[x * cal[i]] = 0
        # elif i == 1 or i == 3:
        #     calculate(x + cal[i], cnt + 1)
        else:
            if visited[x + cal[i]] == 0:
                visited[x + cal[i]] = 1
                calculate(x + cal[i], cnt + 1)
                visited[x + cal[i]] = 0

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    min_cnt = 10e9
    visited = [0] * 1000001
    calculate(N, 0)

    # visited = [0] * 4
    # count = 0
    # check = 0
    #
    # while True:
    #     if check == M:
    #         min(min_cnt, count)
    #         break
    #
    #     for i in range(4):
    #         if i == 2:
    #             check = N * i
    #             count += 1
    #         else:
    #             check = N + i
    #             count += 1

    print(f"#{tc} {min_cnt}")
