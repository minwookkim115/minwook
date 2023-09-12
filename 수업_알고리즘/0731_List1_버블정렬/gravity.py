N = int(input())

arr = list(map(int, input().split()))

start_idx = 0
max_v = 0

for i in range(N):
    big_count = 0
    start_idx += i
    for j in range(i + 1, N):
        if arr[i] <= arr[j]:
            big_count += 1

    if (N - (start_idx + 1)) - big_count > max_v:
        max_v = (N - (start_idx + 1)) - big_count

print(max_v)