T = int(input())

for test_case in range(1, T + 1):

    num_list = list(map(int, input().split()))

    sum = 0

    for x in num_list:
        if x % 2 == 1:
            sum += x
    print(f"#{test_case}", sum)
