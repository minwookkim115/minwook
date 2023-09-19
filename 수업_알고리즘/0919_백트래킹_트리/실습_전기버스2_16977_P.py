import sys

sys.stdin = open("16977_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    charge = list(map(int, input().split()))
    N = charge.pop(0)

    # 충전 횟수
    count = 0
    # 내 지금 위치 인덱스
    now = 0
    # 가야될 곳 인덱스
    go_idx = 0
    # 도착했는지 판별
    arrive = 0

    while True:
        # 도착하면
        if arrive >= N - 1:
            # 끝내기
            break
        # 아니면
        else:
            # 내 지금 위치를 바꿔주면서 이동
            now = go_idx

        # 갈수 있는 최대 값
        go = 0
        # 현재 위치부터 충전지로 갈수 있는만큼 돌면서
        for i in range(now + 1, now + charge[now] + 1):
            # 최대한 멀리 갈수 있는 값 찾기
            if go <= i + charge[i]:
                go = i + charge[i]
                # 찾은 i를 가야할 인덱스로
                go_idx = i

        # 최대한 멀리갈 수 있는 값
        arrive = go
        # 갈때마다 충전 + 1
        count += 1

    print(f"#{tc} {count}")