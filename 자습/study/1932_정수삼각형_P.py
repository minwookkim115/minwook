N = int(input())
tri = [list(map(int, input().split())) for _ in range(N)]

check = []

for i in range(1, N + 1):
    check.append([0] * i)


if N == 1:
    print(tri[0][0])
else:
    for i in range(1, N):
        for j in range(i):
            if i == 1:
                check[i][j] = tri[i - 1][j] + tri[i][j]
                check[i][j + 1] = tri[i - 1][j] + tri[i][j + 1]
            else:
                check[i][j] = max(check[i][j], check[i - 1][j] + tri[i][j])
                check[i][j + 1] = max(check[i][j + 1], check[i - 1][j] + tri[i][j + 1])

    print(max(check[N - 1]))
