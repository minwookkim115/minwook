import sys

sys.stdin = open("algo2_sample_in.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    # 바운스 챌린지 횟수
    N = int(input())

    # 숫자들의 리스트
    numbers = list(map(int, input().split()))

    # 총합
    result = 0

    # 챌린지는 N번 시도
    # N번 시도할 때마다 합을 구하는 방식이 다르다
    # 처음에는 1칸 씩 증가
    # 2칸씩 증가
    # 3칸씩 증가...
    for i in range(N):
        # i번째 챌린지의 합을 구하는 방식
        # i + 1만큼 움직이면서 합을 구한다
        for j in range(0, N, i + 1):
            result += numbers[j]

    result = result if result >= 0 else 0

    print(f"#{tc} {result}")

