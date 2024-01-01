N = int(input())
M = int(input())

virus = [[] for _ in range(N + 1)]
for i in range(M):
    s, e = map(int, input().split())
    virus[s].append(e)
    virus[e].append(s)

check = [0 for _ in range(N + 1)]


def infection(n):
    check[n] = 1
    for com in virus[n]:
        if check[com] == 0:
            infection(com)


infection(1)
print(sum(check) - 1)
