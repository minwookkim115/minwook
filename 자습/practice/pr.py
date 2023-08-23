import sys

sys.stdin = open("input.txt", "r")

maching = {"0001101": 0, "0011001": 1, "0010011": 2,
           "0111101": 3, "0100011": 4, "0110001": 5,
           "0101111": 6, "0111011": 7, "0110111": 8, "0001011": 9}


def maching_result(init):
    for j in maching:
        for i in range(len(mouem)):
            if init[i] == j:
                init[i] = maching[j]
    return init


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    pass_cord = [list(map(int, input())) for _ in range(n)]

    # print(n, m)
    sr = 0
    sc = 0
    for r in range(n):
        for c in range(m - 1, -1, -1):
            if pass_cord[r][c] == 1:
                sr, sc = r, c
                break
    # print(sr, sc)

    pass_list = pass_cord[sr][sc - 55:sc + 1]
    # print(pass_list)
    joy = ""
    for i in range(len(pass_list)):
        c = pass_list[i]
        joy += str(c)

    # print(joy)

    l_pass = len(pass_list)
    mouem = []
    for i in range(0, l_pass, 7):
        pass_word = joy[i:i + 7]
        mouem.append(pass_word)
    # print(mouem)
    a = maching_result(mouem)
    print(a)

    jjaksum = 0
    holsum = 0
    for i in range(len(a)):
        if i % 2 == 0:
            holsum += a[i]
        else:
            jjaksum += a[i]

    print(holsum, jjaksum)
    answer = 0
    if (holsum * 3 + jjaksum) % 10 == 0:
        answer = holsum + jjaksum
    else:
        answer = 0

    print(f"#{tc} {answer}")