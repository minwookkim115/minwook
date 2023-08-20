import sys
sys.stdin = open("16370_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = input()
    M = input()

    max_v = 0

    for i in N:
        count = 0
        for j in M:
            if i == j:
                count += 1

        if max_v <= count:
            max_v = count

    print(f"#{tc} {max_v}")
