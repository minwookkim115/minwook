# 정류장은 1 ~ 5000

# A(출발) B(도착) A ~ B 의 노선
# P => 정류장의 개수
# P 아래 수 => 정류장 번호

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bus_station = [0] * 5001  # 1 ~ 5000번 각 정류장을 지나는 노선 수
    for _ in range(N):  # N개의 노선에 대해
        A, B = map(int, input().split())  # A와 B를 받아옴
        for i in range(A, B + 1):
            bus_station[i] += 1  # 현재 노선이 i번 정류장 정착

    P = int(input())
    bus_stop = [int(input()) for _ in range(P)]

    print(f"#{tc}", end=' ')
    for x in bus_stop:
        print(bus_station[x], end=' ')
    print()  # 넌 왜쓰는 거냐 / 왜쓰긴 왜씀 한줄로 나오니까 두줄로 나오게 하려고 쓰지

