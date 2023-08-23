import sys

sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * (M + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M + 2)]

    print(arr)
