N = int(input())
num_l = list(map(int, input().split()))
operator = list(map(int, input().split()))

max_result = -1000000000
min_result = 1000000000


def find(num, idx):
    global max_result, min_result

    if idx == N:
        max_result = max(max_result, num)
        min_result = min(min_result, num)

    if operator[0] >= 1:
        operator[0] -= 1
        find(num + num_l[idx], idx + 1)
        operator[0] += 1
    if operator[1] >= 1:
        operator[1] -= 1
        find(num - num_l[idx], idx + 1)
        operator[1] += 1
    if operator[2] >= 1:
        operator[2] -= 1
        find(num * num_l[idx], idx + 1)
        operator[2] += 1
    if operator[3] >= 1:
        operator[3] -= 1
        # find(int(num / num_l[idx]), idx + 1)
        # operator[3] += 1
        if num < 0:
            find(-(-num // num_l[idx]), idx + 1)
            operator[3] += 1
        else:
            find(num // num_l[idx], idx + 1)
            operator[3] += 1


find(num_l[0], 1)
print(max_result)
print(min_result)