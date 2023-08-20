import sys
sys.stdin = open("16505_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    N_1 = N // 10

    num = 0

    for i in range(1, N_1 + 1):
        if i == 1:
            num += 1

        if i >= 2:
            if i % 2 == 0:
                num = (num * 2) + 1
            else:
                num = (num * 2) - 1
    print(f"#{tc} {num}")
