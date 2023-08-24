import sys
sys.stdin = open("12421_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input()[:M] for _ in range(N)]

    print(N, M)
    print(arr)

    for r in range(N):
        for c in range(M):
            dec = int(arr[r][c], 16)
            print(dec)
