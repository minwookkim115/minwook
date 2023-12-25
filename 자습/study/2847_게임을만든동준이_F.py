N = int(input())
score = [int(input()) for _ in range(N)]

answer = 0
for i in range(N - 2, -1, -1):
    if score[i] >= score[i + 1]:
        sub = score[i]
        score[i] = score[i + 1] - 1
        answer += sub - score[i]
print(answer)