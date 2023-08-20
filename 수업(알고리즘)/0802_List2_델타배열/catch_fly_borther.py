t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    fly_party = [list(map(int, input().split())) for _ in range(n)]

    all_ground = 0  # 최댓값
    for k in range(n - m + 1):  # 큰 상자 행 이동
        for l in range(n - m + 1):  # 큰 상자 열 이동
            temp = 0
            # 작은 상자 행 이동 / 큰 상자의 첫 행 k 부터 m 만큼
            for i in range(k, k + m):
                # 작은 상자 열 이동 / 큰 상자의 첫 열 l 부터 m 만큼
                for j in range(l, l + m):
                    # 큰 상자의 k 부터 m 만큼 이동한 행 i
                    # 큰 상자의 l 부터 m 만큼 이동한 열 j
                    # => 작은 상자 하나
                    temp += fly_party[i][j]

            print(temp)

    #         # 최댓값 구하기
    #         if temp > all_ground:
    #             all_ground = temp
    #
    # print(f"#{tc} {all_ground}")
