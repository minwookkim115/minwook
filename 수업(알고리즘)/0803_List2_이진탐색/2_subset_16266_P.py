A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    n = len(A)

    count = 0

    for i in range(1 << n):
        sum = 0
        one_count = 0
        for j in range(n):
            if i & (1 << j):
                sum += A[j]
                one_count += 1

        if sum == K and one_count == N:
            count += 1

    print(f"#{tc} {count}")
