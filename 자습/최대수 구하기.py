T = int(input())

for test_case in range(1, 1 + T):

    num_list = list(map(int, input().split()))

    maximum = max(num_list)

    print(f"#{test_case}", maximum)