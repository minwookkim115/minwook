# 인접행렬
# 장점 : 구현이 쉽다
# 단점 : 메모리 낭비 / 0(갈수 없는 곳)도 표시를 하기 때문에
# graph = [
#     [0, 1, 0, 1, 0],
#     [1, 0, 1, 1, 1],
#     [0, 1, 0, 0, 0],
#     [1, 1, 0, 0, 1],
#     [0, 1, 0, 1, 0]
# ]

# 인접 리스트
# 내가 갈 수 있는 지점만 저장하자
# 주의 사항 => 각 노드마다 갈 수 있는 지점의 개수가 다름
#             range 쓸때 index 조심
# 메모리적으로 인접 행렬에 비해 훨씬 효율적이다
graph = [
    [1, 3],
    [0, 2, 3, 4],
    [1],
    [0, 1, 4],
    [1, 3]
]

# 딕셔너리로도 사용 가능
graph_dict = {
    '0': [1, 3],
    '1': [0, 2, 3, 4],
    '2': [1],
    '3': [0, 1, 4],
    '4': [1, 3]
}

# DFS
# stack 버전
def dfs_stack(start):
    visited = []
    stack = [start]

    while stack:
        now = stack.pop()  # pop 0 돌려보기
        # 이미 방문한 지점이라면 continue
        if now in visited:
            continue

        # 방문하지 않은 지점이라면, 방문 표시
        visited.append(now)

        # 갈 수 있는 곳들을 stack에 추가
        # for next in range(5): => 큰번호부터 진행
        # for next in range(4, -1, -1): => 작은번호부터 진행
        for to in range(len(graph[now]) - 1, -1, -1):
            # 연결이 안되어 있다면 continue
            # 인접 리스트를 사용하게 되면 연결 안돼있는걸 판단할 필요 없다.
            # if graph[now][next] == 0:
            #     continue

            next = graph[now][to]
            # 방문한 지점이라면 스택에 추가하지 않음
            if next in visited:
                continue

            stack.append(next)
    # 출력을 위한 반환
    return visited


print("def_stack = ", end='')
print(dfs_stack(0))

# DFS - 재귀
# MAP 크기(길이)를 알 때
# append 형식 말고 아래와 같이 사용하면 훨씬 빠름
visited = [0] * 5
path = []  # 방문 순서 기록


def dfs(now):
    visited[now] = 1  # 현재 지점 방문 표시
    print(now, end=' ')

    # 인접한 노드들을 방문
    for to in range(len(graph[now])):
        # 인접 리스트 쓸때는 필요 없음
        # if graph[now][next] == 0:
        #     continue

        next = graph[now][to]
        if visited[next]:
            continue

        dfs(next)


print("def_재귀 = ", end=' ')
dfs(0)
