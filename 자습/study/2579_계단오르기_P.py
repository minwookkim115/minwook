N = int(input())
point = [int(input()) for _ in range(N)]

check = [0] * N

if N <= 2:
    print(sum(point))
else:
    check[0] = point[0]
    check[1] = point[0] + point[1]
    for i in range(2, N):
        # i 번째 가는 최대값 check에 넣기
        check[i] = max(check[i - 3] + point[i - 1] + point[i], check[i - 2] + point[i])

    print(check[N - 1])
