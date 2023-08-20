T = 10

for tc in range(1, T + 1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    best_max_v = 0

    max_list = []  # 가장 큰 행합, 열 합, 대각선 합, 역 대각선 합 리스트

    max_sum_r = 0  # 가장 큰 행 합
    max_sum_c = 0  # 가장 큰 열 합
    sum_d = 0  # 대각선 합
    sum_d_rev = 0  # 역 대각선 합

    for r in range(100):
        sum_r = 0  # 행 합
        sum_c = 0  # 열 합
        for c in range(100):
            sum_r += arr[r][c]
            sum_c += arr[c][r]

            if max_sum_r < sum_r:
                max_sum_r = sum_r
            if max_sum_c < sum_c:
                max_sum_c = sum_c

    for i in range(100):
        sum_d += arr[i][i]
        sum_d_rev += arr[i][99 - i]

    max_list.append(max_sum_r)
    max_list.append(max_sum_c)
    max_list.append(sum_d)
    max_list.append(sum_d_rev)

    # max_list에서 가장 큰 값
    for i in max_list:
        if i > best_max_v:
            best_max_v = i

    print(f"#{tc} {best_max_v}")
