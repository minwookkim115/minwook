N = 2  # 행의 크기
M = 4  # 열의 크기
arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
# [[0, 1, 2, 3]
#  [4, 5, 6, 7]]

# i 는 행
# j 는 열

for i in range(N):
    for j in range(M):
        print(arr[i][j])  # 0123 4567

for j in range(M):
    for i in range(N):
        print(arr[i][j])  # 04 15 26 37 / 열 고정

for i in range(N):
    for j in range(M):
        print(arr[i][j + (M - 1 - 2 * j) * (i % 2)])
        # 0123 7654
        # 짝수는 오른쪽으로, 홀수는 왼쪽으로

for i in range(N):
    for j in range(M):
        if i % 2 == 1:  # 홀수 번 행인 경우
            print(arr[i][M - 1 - j])
            # 7654
        else:
            print(arr[i][j])
            # 0123


max_v = 0
for i in range(N):
    row_total = 0   # 각 행의 합
    for j in range(M):
        row_total += arr[i][j]
    if max_v < row_total:
        max_v = row_total
print(max_v)