import sys

sys.stdin = open('in2.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    n = len(arr)

    answer = 0

    for i in range(1, 1 << n):
        sum = 0
        for j in range(n):
            if i & (1 << j):
                sum += arr[j]

        if sum == 0:
            answer = 1

    print(answer)