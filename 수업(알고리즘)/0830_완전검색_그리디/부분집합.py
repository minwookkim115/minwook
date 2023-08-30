a = [3, 6, 7, 1, 5, 4]
N = 6

# for i in range(1, (1 << N) - 1):  # 공집합 빼고
for i in range(1, 1 << (N - 1)): # 1 << (N-1) == (1 << N) // 2
    group1 = []
    group2 = []
    total1 = 0
    total2 = 0
    min_v = 100
    for j in range(N):
        if i & (1 << j):  # j번 비트가 0이 아니면
            group1.append(a[j])
            total1 += a[j]
        else:
            group2.append(a[j])
            total2 += a[j]
    r1 = group1
    r2 = group2
    if r1 and r2:
        if min_v > abs(total1 - total2):
            min_v = abs(total1 - total2)
    print(min_v)
    print(group1, group2)
