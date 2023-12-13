N = int(input())
time = list(map(int, input().split()))
time.sort()

answer = 0
for i in range(N):
    answer += time[i] * (N - i)

print(answer)