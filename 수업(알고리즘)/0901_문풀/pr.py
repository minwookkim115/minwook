import sys

sys.stdin = open("4013_input.txt", "r")


# 돌리는 함수
# a : 돌릴 리스트
# b : 시계방향, 반시계방향
def turn(a, b, c):
    if b == 1:
        a.insert(0, a[7])
        a.pop()
    else:
        a.append(a[0])
        a.pop(0)
    mag[c] = a
    return


def magnetic(a, b, c):
    finish[a-1] = 1
    if a == 1:
        if finish[a] != 1:
            if mag[a - 1][2] != mag[a][6]:
                magnetic(a + 1, -b, c+1)
                turn(mag[a - 1], b, a - 1)
            else:
                if c != 0:
                    turn(mag[a - 1], b, a - 1)
    if a == 2:
        if finish[a - 2] != 1:
            if mag[a-1][6] != mag[a - 2][2]:
                magnetic(a - 1, -b, c+1)
                turn(mag[a - 1], b, a - 1)
            else:
                if c != 0:
                    turn(mag[a - 1], b, a - 1)

        if finish[a] != 1:
            if mag[a - 1][2] != mag[a][6]:
                magnetic(a + 1, -b, c+1)
                turn(mag[a - 1], b, a - 1)
            else:
                if c != 0:
                    turn(mag[a - 1], b, a - 1)
    if a == 3:
        if finish[a - 2] != 1:
            if mag[a-1][6] != mag[a - 2][2]:
                magnetic(a - 1, -b, c+1)
                turn(mag[a - 1], b, a - 1)
            else:
                if c != 0:
                    turn(mag[a - 1], b, a - 1)
        if finish[a] != 1:
            if mag[a - 1][2] != mag[a][6]:
                magnetic(a + 1, -b, c+1)
                turn(mag[a - 1], b, a - 1)
            else:
                if c != 0:
                    turn(mag[a - 1], b, a - 1)
    if a == 4:
        if finish[a - 2] != 1:
            if mag[a-1][6] != mag[a - 2][2]:
                magnetic(a - 1, -b, c+1)
                turn(mag[a - 1], b, a - 1)
            else:
                if c != 0:
                    turn(mag[a - 1], b, a - 1)


T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    mag = [list(map(int, input().split())) for _ in range(4)]

    for i in range(K):
        finish = [0] * 4
        a, b = map(int, input().split())
        magnetic(a, b, 0)
    print(mag)

    answer_l = []
    for i in range(4):
        answer_l.append(mag[i][0])

    print(answer_l)