import sys

sys.stdin = open("16788_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = float(input())

    bin1 = ""

    i = 0
    while True:
        N = N * 2
        if N >= 1:
            bin1 += "1"
            N -= 1
        elif N > 0:
            bin1 += "0"
        elif N == 0:
            break

        i += 1

        if i >= 13:
            bin1 = "overflow"
            break

    print(f"#{tc} {bin1}")
