N, M = map(int, input().split())
cards = list(map(int, input().split()))

bit = [0] * N

answer = 0


def find(i, n, subsum, k):
    global answer

    if subsum > M:
        return

    if k == 3:
        answer = max(answer, subsum)
        return

    if i == n:
        return

    bit[i] = 1
    find(i + 1, n, subsum + cards[i], k + 1)
    bit[i] = 0
    find(i + 1, n, subsum, k)


find(0, N, 0, 0)
print(answer)
