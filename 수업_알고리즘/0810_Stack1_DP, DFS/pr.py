def dfs(s, V):
    visited = [0] * V
    stack = []

    visited[s] = 1
    print(node[s])

    i = s

    while True:
        for j in range(V):

            if adj_m[i][j] == 1 and visited[j] == 0:
                stack.append(i)
                print(node[j])
                visited[j] = 1
                i = j
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break
    return

#         A  B  C  D  E  F  G
adj_m = [[0, 1, 1, 0, 0, 0, 0],  # A
         [1, 0, 0, 1, 1, 0, 0],  # B
         [1, 0, 0, 0, 1, 0, 0],  # C
         [0, 1, 0, 0, 0, 1, 0],  # D
         [0, 1, 1, 0, 0, 1, 0],  # E
         [0, 0, 0, 1, 1, 0, 1],  # F
         [0, 0, 0, 0, 0, 1, 0]   # G
         ]
node = ["A", "B", "C", "D", "E", "F", "G"]
N = 7
dfs(0, N)