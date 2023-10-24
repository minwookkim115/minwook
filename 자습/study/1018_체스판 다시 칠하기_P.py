N, M = map(int, input().split())
chess = [list(map(str, input())) for _ in range(N)]

perfect_chess = [['']*8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0:
                perfect_chess[i][j] = 'B'
            else:
                perfect_chess[i][j] = 'W'
        else:
            if j % 2 == 0:
                perfect_chess[i][j] = 'W'
            else:
                perfect_chess[i][j] = 'B'

answer = 100

for i in range(N - 7):
    for j in range(M - 7):
        sub_count = 0
        for r in range(i, i + 8):
            for c in range(j, j + 8):
                if chess[r][c] != perfect_chess[r-i][c-j]:
                    sub_count += 1

        count = min(sub_count, (64-sub_count))
        answer = min(count, answer)

print(answer)