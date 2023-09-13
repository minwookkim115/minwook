N, M = map(int, input().split())

num_l = []
for i in range(1, N + 1):
    num_l.append(i)

for _ in range(M):
    s, e = map(int, input().split())
    numl = num_l[s-1:e]
    numl.reverse()
    num_l[s-1:e] = numl

for i in range(N):
    print(num_l[i], end=" ")