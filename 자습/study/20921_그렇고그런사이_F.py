# 시간초과
N, K = map(int, input().split())

answer = []


def couple(n, k):
    while True:
        if k >= n:
            answer.append(n)
            n, k = (n - 1), (k - (n - 1))
        else:
            answer.append(k + 1)
            for i in range(1, k + 1):
                answer.append(i)
            for i in range(k + 2, k + 1):
                answer.append(i)
        if len(answer) == N:
            break


couple(N, K)
print(answer)
