import sys

sys.stdin = open("1219_input.txt", "r")

T = 10

for tc in range(1, T + 1):
    t, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adj_l = [[] for _ in range(100)]
    for i in range(E):
        s, e = arr[i * 2], arr[i * 2 + 1]
        adj_l[s].append(e)

    def dfs(s, v):
        visited = [0] * (v + 1)
        stack = []

        i = s
        visited[i] = 1

        while True:
            for j in adj_l[i]:
                if visited[j] == 0:
                    stack.append(i)
                    i = j
                    visited[j] = 1
                    break
            else:
                if stack:
                    i = stack.pop()
                else:
                    break

        if visited[v] == 1:
            return 1
        else:
            return 0


    print(f"#{tc} {dfs(0, 99)}")
