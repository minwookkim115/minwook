N, M = map(int, input().split())
chess = [list(map(str, input())) for _ in range(M)]

count = 1000000
for i in range(N - 7):
    for j in range(M - 7):
        check = chess[i][j]
        sub_count = 0
        for r in range(i, i + 8):
            for c in range(j + 1, j + 8):
                if chess[r][c] != check:
                    check = chess[r][c]
                else:
                    sub_count += 1
                    if check == 'B':
                        check = 'W'
                    else:
                        check = 'B'
        count = min(count, sub_count)

print(count)