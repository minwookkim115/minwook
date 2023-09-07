N, M = map(int, input().split())

num_l = []
for i in range(1, N + 1):
    num_l.append(i)

sl = []
el = []
for _ in range(M):
    s, e = map(int, input().split())
    sl.append(s)
    el.append(e)

for i in range(M):
    if sl[i] % 2 == 1:
        for j in range(sl[i]-1, )