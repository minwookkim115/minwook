N = int(input())
arr = list(map(int, input().split()))
check = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            check[i] = max(check[i], check[j] + 1)

print(max(check))