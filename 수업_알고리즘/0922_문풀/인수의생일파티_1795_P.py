import sys

sys.stdin = open("1795_input.txt", "r")

import heapq


# 다익스트라
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 0: 가중치, start: 시작정점
    D[start] = 0  # start에서 start는 0이니까

    # q가 빌때까지
    while q:

        # q에 들어있는
        # w: 가중치, v: 현재 위치
        w, v = heapq.heappop(q)

        # 내가 가야할 v번 노드까지의 가중치 w가
        # 이미 저장해둔거 보다 크면 계산할 필요 x
        if D[v] < w:
            continue

        # u: v에서 갈 정점 번호
        # uw: 가중치
        for u, uw in adjl[v]:
            cost = D[v] + uw
            if cost < D[u]:
                D[u] = cost
                heapq.heappush(q, (cost, u))


T = int(input())

for tc in range(1, T + 1):
    # N: 정점 수
    # M: 노드 수
    # X: 출발 점
    N, M, X = map(int, input().split())

    # 인덱스 별로 가야할 노드와 가중치 넣기
    adjl = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        adjl[x].append((y, c))

    # 갈때 하고 올때 체크하기위한 배열
    check = [0] * (N + 1)

    # dijkstra를 모든 정점에서 돌려본다.
    for i in range(1, N + 1):
        D = [0] + [1000000] * N
        # 주어진 출발 정점(X)에서 dijkstra는
        # 출발 정점에 그대로 삽입
        if i == X:
            dijkstra(i)
            for j in range(len(D)):
                check[j] += D[j]
        # 다른 곳에서 출발 정점(X) 로 오는 값을 구하기 위해
        # check의 i 번째(각 정점)에
        # D[X](각 정점에서 2번을 갈수 있는 최솟값)을 더해주기
        else:
            dijkstra(i)
            check[i] += D[X]

    print(f"#{tc} {max(check)}")
