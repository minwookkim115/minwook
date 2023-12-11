def answer(n, m):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(1, n + 1):
        if len(arr) > 0 and i >= max(arr):
            arr.append(i)
            answer(n, m)
            arr.pop()
        elif len(arr) == 0:
            arr.append(i)
            answer(n, m)
            arr.pop()


N, M = list(map(int, input().split()))
arr = []

answer(N, M)
