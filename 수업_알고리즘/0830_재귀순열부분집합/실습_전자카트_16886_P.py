import sys

sys.stdin = open("16886_input.txt", "r")


# 순열을 만들어서
# 순열 == 갈수있는 관리구역
def battery(i, n):
    global min_use_battery
    global use_battery
    # 순열이 구해 졌을때
    # [1, 2, 3, 1] or [1, 3, 2, 1] 처럼
    # ==> 1에서2갔다 2에서3갔다 3에서1로 복귀
    # ==> 1에서3갔다 3에서2갔다 2에서1로 복귀
    if i == n:
        for k in range(N):
            # area(1,2) + area(2,3) + area(3,1)
            use_battery += area[can_go[k] - 1][can_go[k + 1] - 1]
        if min_use_battery > use_battery:
            min_use_battery = use_battery
        use_battery = 0
    # 순열 구하기
    else:
        for j in range(N):
            # j가 안간곳이면
            if used[j] == 0:
                # 갈수있는 곳에
                # j 집에 넣기
                can_go[i] = arr[j]
                # 사용했다고 체크 하고
                used[j] = 1
                # 재귀
                battery(i + 1, n)
                # 끝날때 마다 사용한거 다시 사용안했다고
                used[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]

    use_battery = 0  # 현재 쓴 배터리
    min_use_battery = 1000  # 최소 배터리

    arr = []  # 순열을 만들기 위한 배열
    for i in range(1, N + 1):
        arr.append(i)

    # 순열을 만들기 위해 사용한 것 체크
    # 1은 사무실 고정이니까 앞에 1 붙이고
    used = [1] + [0] * (N - 1)
    # 갈 수 있는곳 탐색하는 배열
    # 1은 사무실 고정 앞에 1
    # 뒤에 사무실 도착해야 하니까 뒤에 고정 1
    can_go = [1] + [0] * (N - 1) + [1]
    battery(1, N)

    print(f"#{tc} {min_use_battery}")
