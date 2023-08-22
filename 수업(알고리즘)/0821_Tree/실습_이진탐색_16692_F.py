import sys
sys.stdin = open("16692_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    lst = [0] * (N + 1)

    val = 0
