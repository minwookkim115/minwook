def subset(i, N):
    global count
    if i == N:
        s = 0
        for j in range(N):
            if bit[j]:
                s += arr[j]
        if s == 0:
            count += 1
            for j in range(N):
                if bit[j]:
                    subs.append(arr[j])
            print(subs)
            subs.clear()
    else:
        bit[i] = 1
        subset(i+1, N)
        bit[i] = 0
        subset(i+1, N)


arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
bit = [0] * N
subs = []
count = 0
subset(0, N)
print(count)