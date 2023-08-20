arr = list(map(int, input().split()))

max_v = 0
arr_len = len(arr)

for i in arr:
    if i > max_v:
        max_v = i

counts = [0] * (max_v + 1)

for i in range(arr_len):
    counts[arr[i]] += 1

for i in range(1, len(counts)):
    counts[i] += counts[i - 1]

new_arr = [0] * 8

for i in range(arr_len-1, -1, -1):
    counts[arr[i]] -= 1
    new_arr[counts[arr[i]]] = arr[i]

print(new_arr)