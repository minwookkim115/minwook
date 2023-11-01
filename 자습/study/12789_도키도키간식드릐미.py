N = int(input())

numbers = list(map(int, input().split()))

check_list = sorted(numbers)
stack = []
check = []

i = 0
j = 0
while i < N:
    if numbers[i] != check_list[j]:
        if stack and check and i != 0 and check[-1] + 1 == stack[-1]:
            check.append(stack[-1])
            stack.pop()
        else:
            stack.append(numbers[i])
            i += 1
    elif numbers[i] == check_list[j]:
        check.append(numbers[i])
        j += 1
        i += 1

for k in range(len(stack) - 1, -1, -1):
    check.append(stack[k])

if check == check_list:
    print("Nice")
else:
    print("Sad")