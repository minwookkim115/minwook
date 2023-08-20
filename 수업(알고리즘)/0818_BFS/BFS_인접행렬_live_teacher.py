'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def bfs(s, V):
    visited = [0] * (V + 1)
    q = []
    q.append(s)
    visited[s] = 1
    while q:
        t = q.pop(0)
        print(t)
        for w in range(1, V + 1):
            if visited[t][w] == 1 and


V, E = map(int, input().split())
arr = list(map(int, input().split()))

adj_m = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1