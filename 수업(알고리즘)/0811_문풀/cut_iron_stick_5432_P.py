# 레이저가 나오면 그동안 쌓인 쇠막대기('(')의 수
# 조각이 닫히면 + 1 / 남은 조각은 - 1
# 다시 쇠막대기를 쌓고 레이저를 만나면 쌓인 쇠막대기 수

import sys

sys.stdin = open("5432_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    lst = list(map(str, input()))

    stick_start = 0
    piece = 0

    for i in range(len(lst)):
        if lst[i] == "(":
            stick_start += 1
            if lst[i] == "(" and lst[i + 1] == ")":
                stick_start -= 1
                piece += stick_start
        if lst[i] == ")":
            piece += 1
            stick_start -= 1
            if lst[i] == ")" and lst[i - 1] == "(":
                piece -= 1
                stick_start += 1

    print(f"#{tc} {piece}")
