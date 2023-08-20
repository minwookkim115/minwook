T = int(input())

for test_case in range(1, 1+T):
    
    num1, num2 = map(int, input().split())

    quota = num1 // num2
    rest = num1 % num2

    print(f"#{test_case} {quota} {rest}")