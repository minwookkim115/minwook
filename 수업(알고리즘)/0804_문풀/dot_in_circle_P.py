import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    dot_count = 0

    for x in range(-N, N + 1):
        for y in range(-N, N + 1):
            if x ** 2 + y ** 2 <= N ** 2:
                dot_count += 1

    print(f"#{tc}", dot_count)
