T = 10

for tc in range(1, T + 1):
    # 덤프 횟수(상자를 옮겨야 하는 횟수)
    N = int(input())

    # 각 상자들의 높이가 주어진다.
    box = list(map(int, input().split()))

    # N 이 0보다 크면 덤프 횟수가 남아있다.
    # N 이 0이 될 때까지 평탄화 작업을 계속 한다. (한버 할 때마다 N 을 1씩 감소 시키기)
    while N > 0:

        # 제일 높은 상자가 어디있는데
        max_idx = 0
        # 상자 높이 최대값
        max_height = 0
        # 제일 낮은 상자가 어디있는데
        min_idx = 0
        # 상자 높이 최소값
        min_height = 100

        # 가로의 길이(100) 만큼 반복하면서 최대값, 최소값 찾기
        # 상자를 옮기면 높이가 변하기 때문에 그 위치도 기억 해놔야 한다.
        for i in range(100):
            # i 번째 상자의 높이 : box[i]
            # i 번째 상자의 높이가 지금까지 알고 있던 최대 높이 상자높이보다 높으면 갱신
            if box[i] > max_height:
                max_height = box[i]
                max_idx = i  # 제일 높은 상자 위치 기억

            if box[i] < min_height:
                min_height = box[i]
                min_idx = i  # 제일 낮은 상자 위치 기억

        # 100개의 상자를 다 확인하고 나서
        # 제일 높은 위치에 있는 상자 하나를 제일 낮은 위치에 있는 곳으로 옮긴다.

        # 제일 높은 곳 높이 -1, 제일 낮은 곳 높이 +1
        box[max_idx] -= 1
        box[min_idx] += 1

        # 상자 한번 옮기기 끝
        N -= 1

    # 평탄화 작업 끝
    # 마지막 부분에서 최대값과 최소값을 한 번 더 구해줘야 함
    # 옮기기 전 높이 != 옮긴 후 높이

    max_height = 0
    min_height = 100

    for i in range(100):
        if box[i] > max_height:
            max_height = box[i]

        if box[i] < min_height:
            min_height = box[i]

    print(f"#{tc} {max_height - min_height}")
