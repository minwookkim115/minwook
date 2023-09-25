import sys

sys.stdin = open("algo1_sample_in.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P = list(input())
    key = int(input(), 16)

    H = [0] * N

    for i in range(N):
        H[i] = int(P[i], 16) ^ key  # xor연산은 다시 하면 복원된다.

    print(f"#{tc}", end=' ')
    for x in H:
        print(f"{x:X}", end="")
    print()