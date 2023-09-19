import sys

sys.stdin = open("1767_input.txt", "r")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]




T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    mex = [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    print(N, mex)