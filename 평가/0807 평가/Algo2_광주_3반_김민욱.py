import sys
sys.stdin = open("algo2_sample_in.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    point = list(map(int, input().split()))

    sum = 0  # 챌린지 합

    for i in range(1, N + 1):  # 늘어나는 공던지기 간격
        for j in range(N):
            if j % i == 0:  # 길이가 N인 배열에서 0을 포함하여 i의 배수가 되는 인덱스 값 j
                sum += point[j]  # i의 배수가 되는 인덱스 j 값의 합

    if sum <= 0:    # 0 이하면 0 출력
        print(f"#{tc}", "0")
    else:   # 0 이상이면 합 출력
        print(f"#{tc} {sum}")
