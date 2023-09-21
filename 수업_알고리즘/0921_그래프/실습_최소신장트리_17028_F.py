import sys

sys.stdin = open("17028_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [[0] * V for _ in range(V)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        arr[s][e] = w
        arr[e][s] = w