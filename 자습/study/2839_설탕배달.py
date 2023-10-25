N = int(input())

count = 0

check_n = 0

while True:
    if N >= 5:
        check_n = N % 5
        count = N // 5
    else:
        if N == 3:
            count = 1
        else:
            count = -1

    if check_n == 0:
        break
    elif check_n == 1:
        count += 1
        break
    elif check_n == 2:
        count = 2000
        break
    elif check_n == 3:
        count += 1
        break
    elif check_n == 4:
        count = 2000
        break

if count == 2000:
    sub_count = 0
    if N % 3 == 0:
        sub_count = N // 3
        count = min(count, sub_count)
    if N >= 12 and (N - 12) % 5 == 0:
        sub_count = (N - 12) // 5
        sub_count += 4
        count = min(count, sub_count)
    if N >= 9 and (N - 9) % 5 == 0:
        sub_count = (N - 9) // 5
        sub_count += 3
        count = min(count, sub_count)
    if sub_count == 0:
        count = -1

print(count)
