import sys

sys.stdin = open("1220_input.txt", "r")

T = 10
for tc in range(1, T + 1):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]

    count = 0  # 교착 수
    for j in range(n):
        tmp = 0
        for i in range(n):
            if table[i][j] == 2 and tmp == 1:
                count += 1
                tmp = 0
            elif table[i][j] == 1:
                tmp = 1

    print(f"#{tc} {count}")
