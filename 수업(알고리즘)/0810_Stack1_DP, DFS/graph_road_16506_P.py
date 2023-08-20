import sys

sys.stdin = open("16506_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())  # 숫자의 개수(V)와 선의 개수(E)

    adj_l = [[] for _ in range(V + 1)]  # 각 숫자가 갈 수 있는 곳 list
    for i in range(E):
        s, e = map(int, input().split())
        adj_l[s].append(e)
    # print(adj_l)
    S, G = map(int, input().split())  # 숫자의 출발점과 도착점

    def dfs(s, g, v):  # 출발점, 도착점, 숫자 개수를 파라미터로
        visited = [0] * (v + 1)  # 방문했는지 확인 위한 list
        stack = []  # 갈 곳이 없을 때 pop 해서 돌아갈 stack

        i = s  # 주어진 출발점에서 시작
        visited[i] = 1  # 출발점은 방문 했다는 표시

        while True:
            answer = 0  # 갈수 있는지 없는지 판단 할 변수
            for j in adj_l[i]:  # j가 i번째의 인접 리스트를 돌면서
                if j == g:  # j가 도착점 g와 같으면
                    answer += 1  # 갈 수 있다.
                    return answer
                if visited[j] == 0:  # 방문 안했으면
                    stack.append(i)  # 스택에 방금 지나온곳 append
                    i = j  # i 는 움직인곳 j로
                    visited[j] = 1  # 방문했다고 체크
                    break
            else:  # 도착도 못하고, 더이상 갈곳 없을 때
                if stack:  # 스택이 안 비어 있으면
                    i = stack.pop()  # 돌아가고
                else:  # 비어 있으면
                    return answer  # 0의 answer 출력


    print(f"#{tc}", dfs(S, G, V))
