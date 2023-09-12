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
        for w in adj_l[t]:
            if visited[w] == 0
