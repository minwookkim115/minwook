import sys

sys.stdin = open("16673_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())  # V = 노드 개수 / E = 간선 개수
    graph = [[] for _ in range(V + 1)]  # 인접 리스트

    # 인접리스트에 간선 시작점s인덱스에 끝점e를 삽입
    # 방향이 없으므로 간선 끝점e인덱스에도  시작점s를 삽입
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    S, G = map(int, input().split())  # 출발점 S와 도착점 G

    visited = [0] * (V + 1)  # 1부터 시작하므로 V+1 크기의 visited 생성
    q = []
    q.append(S)  # q에 출발점 삽입
    visited[S] = 1  # visited에 출발점 표시

    answer = 0
    while q:  # 큐가 비게되면 모든곳을 방문함
        go = q.pop(0)  # 다음 방문할 곳 q에서 pop

        # 그래프의 다음 방문할곳을 돌면서
        for i in graph[go]:
            # 도착점 G가 있다면
            if visited[i] == 0:
                q.append(i)  # q에 삽입
                visited[i] = visited[go] + 1  # visited[go]에 +1 하여 삽입
        # 갈수가 없으면
        if visited[G] == 0:
            answer = 0
        # 갈수 있으면
        else:
            answer = visited[G] - 1

    print(f"#{tc} {answer}")
