import sys
sys.stdin = open("2117_input.txt", "r")

T = int(input())

# cost[k] = 운영 영역이 k일때 운영 비용
cost = [k * k + (k-1) * (k-1) for k in range(40)]

for tc in range(1, T + 1):
    # N : 도시 크기
    # M : 집 하나당 낼수 있는 비용
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대 집 수
    max_count = 0

    # 집 위치만 계산
    home_lst = []
    for r in range(N):
        for c in range(N):
            # r,c에 집이 있다.
            if arr[r][c] == 1:
                home_lst.append((r, c))

    # 모든위치 (r,c)에서 k=1 ~ k=40 까지 검사
    for r in range(N):
        for c in range(N):
            # dist[k] 거리가 정확히 k일때 포함되는 집의 개수
            dist = [0] * 40

            for hr, hc in home_lst:
                # 거리계산
                k = abs(r-hr) + abs(c-hc) + 1
                # 거리가 정확히 k일때 집 개수 1 증가
                dist[k] += 1

            for k in range(1, 40):
                # 거리가 k일때 포함되는 집 개수 => k-1일때 집 개수 포함
                dist[k] += dist[k-1]
                # 손해만 아니면(이익이 0이어도) 최대 집 개수 계산
                if cost[k] <= dist[k] * M:
                    max_count = max(max_count, dist[k])

    print(f"#{tc} {max_count}")