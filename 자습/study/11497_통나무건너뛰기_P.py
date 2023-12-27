T = int(input())

for _ in range(T):
    N = int(input())
    trees = list(map(int, input().split()))

    trees.sort()

    answer = 0
    for i in range(2, N):
        answer = max(answer, abs(trees[i] - trees[i - 2]))

    print(answer)