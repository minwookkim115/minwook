import sys

sys.stdin = open("GNS_test_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    M, N = map(str, input().split())

    num_list = list(map(str, input().split()))

    count = [0] * 10

    for i in num_list:
        if i == "ZRO":
            count[0] += 1
        if i == "ONE":
            count[1] += 1
        if i == "TWO":
            count[2] += 1
        if i == "THR":
            count[3] += 1
        if i == "FOR":
            count[4] += 1
        if i == "FIV":
            count[5] += 1
        if i == "SIX":
            count[6] += 1
        if i == "SVN":
            count[7] += 1
        if i == "EGT":
            count[8] += 1
        if i == "NIN":
            count[9] += 1

    numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    # for i in range(1, len(count)):
    #     count[i] += count[i - 1]
    #
    # num_str_list = [0] * N + 1

    print(f"#{tc}")
    for i in range(len(count)):
        for _ in range(count[i]):
            print(numbers[i], end=' ')
