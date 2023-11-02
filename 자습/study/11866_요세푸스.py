N, K = map(int, input().split())

arr = []
for i in range(1, N + 1):
    arr.append(i)


check = [0] * N
answer = []
i = 0
count = 0
while True:
    if 0 not in check:
        break

    if check[i] != 1 and count == K-1:
        count = 0
        answer.append(arr[i])
        check[i] = 1

    if check[i] == 0:
        count += 1

    i += 1

    if i >= N:
        i = i % N

print('<', end='')
print(*answer, sep=", ", end='')
print('>')
