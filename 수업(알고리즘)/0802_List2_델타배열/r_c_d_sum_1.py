T = 10

for tc in range(1, T + 1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    best_max_v = 0

    sum_d = 0
    sum_d_rev = 0

    for r in range(100):
        sum_r = 0  # 행 합
        sum_c = 0  # 열 합
        sum_d += arr[r][r]
        sum_d_rev += arr[r][99 - r]

        if best_max_v < sum_d:
            best_max_v = sum_d
        if best_max_v < sum_d_rev:
            best_max_v = sum_d_rev

        for c in range(100):
            sum_r += arr[r][c]
            sum_c += arr[c][r]

            if best_max_v < sum_r:
                best_max_v = sum_r
            if best_max_v < sum_c:
                best_max_v = sum_c

    print(f"#{tc} {best_max_v}")
