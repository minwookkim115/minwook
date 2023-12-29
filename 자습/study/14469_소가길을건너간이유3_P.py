N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]

time.sort(key=lambda x: x[0])

answer = 0
for i in range(N):
    if time[i][0] >= answer:
        answer = time[i][0]
    answer += time[i][1]

print(answer)