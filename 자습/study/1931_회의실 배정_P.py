N = int(input())
meeting = [list(map(int, input().split())) for _ in range(N)]

meeting.sort(key=lambda x: (x[1], x[0]))

answer = 1
finish = meeting[0][1]
for i in range(1, N):
    if meeting[i][0] >= finish:
        answer += 1
        finish = meeting[i][1]

print(answer)