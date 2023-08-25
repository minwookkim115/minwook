import sys

sys.stdin = open("4408_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    count = [0] * 201  # 방사이 공간을 지나는 사람 수를 입력할 복도 공간

    for a, b in arr:  # a <= b라는 보장은 없다
        a = (a + a % 2) // 2
        b = (b + b % 2) // 2
        for i in range(min(a, b), max(a, b) + 1):
            count[i] += 1

    print(f"#{tc} {max(count)}")