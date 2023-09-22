'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

from heapq import heappop, heappush

INF = 10000000  # 무한대 초기화용


# s : 시작 정점
def dijkstra(s):
    q = []
    heappush(q, (0, s))  # (가중치, 정점)
    D[s] = 0  # 시작정점 비용은 0 (s 에서 s 까지 가는데는 가중치가 0)

    while q:
        print(D)

        # w : 가중치 , v : 정점 번호
        w, v = heappop(q)

        # 방금 꺼내온 v번 노드까지의 가중치 w가
        # 이전에 계산해 놓은 v번 까지의 최소 거리보다 크면 계산할 필요 x
        # D[t]는 처음에 무한대로 초기화 해 놨으니까 계산한 적이 있는지 체크도 가능
        if D[v] < w:
            continue

        # v와 연결된 정점을 탐색
        # u : v와 연결된 정점 번호
        # uw : v에서 u까지의 가중치
        for u, uw in adjl[v]:
            cost = D[v] + uw  # v까지의 가중치 + v에서 u까지의 가중치 = v에서 u까지 가는데 가중치
            if cost < D[u]:  # 방금 계산한 거리가 이전에 계산한 거리보다 작으면
                D[u] = cost  # 최단거리 갱신
                heappush(q, (cost, u))  # 최단거리가 갱신된 경우에만 큐에 삽입


V, E = map(int, input().split())
adjl = [[] for _ in range(V)]

for _ in range(E):
    s, e, w = map(int, input().split())
    adjl[s].append((e, w))

print(adjl)

# D[i] = 시작지점 에서 i 까지 가는데 걸리는 최소 비용
D = [INF] * V

dijkstra(0)
print(D)