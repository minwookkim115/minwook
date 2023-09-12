T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 파이썬은 알아서 개수만큼 쪼개줌
    numbers = list(map(int, input().split()))

    # 구간합의 최소, 최대값
    max_sum = 0  # 내가 지금까지 알고 있었던 최대값
    min_sum = 10000 * M  # 내가 지금까지 알고 있었던 최소값

    # 구간합을 구하자 (뒤쪽은 구간합을 M개 고를 수 없을 수 있으니까)
    for i in range(N - M + 1):
        # 시작 위치가 i 일때의 구간합
        sub_sum = 0
        # i 위치에서 M개 골라서 합을 구해준다.
        # i = 현재위치
        # i, i+1, i+2 ......
        # i + j => 구간합에 더할 원소의 위치
        for j in range(M):
            sub_sum += numbers[i + j]

        # if sub_sum > max_sum:
        #     max_sum = sub_sum
        # if sub_sum < min_sum:
        #     min_sum = sub_sum

        # 구간합을 구하고 나서 최대값 최소값 확인
        max_sum = sub_sum if sub_sum > max_sum else max_sum
        min_sum = sub_sum if sub_sum < min_sum else min_sum

    print(f"#{tc} {max_sum - min_sum}")

