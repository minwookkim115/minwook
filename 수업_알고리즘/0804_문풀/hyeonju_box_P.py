import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, Q = map(int, input().split())

    box = [0] * N

    change_box = [list(map(int, input().split())) for _ in range(Q)]

    for i in range(Q):
        for j in range(change_box[i][0] - 1, change_box[i][1]):
            box[j] = (i + 1)

    box_value = []

    for i in box:
        box_value.append(str(i))

    print(f"#{tc}", " ".join(box_value))

