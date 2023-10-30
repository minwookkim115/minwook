T = int(input())

for _ in range(T):
    string = input()
    stack = []
    answer = 'YES'
    for i in string:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                answer = 'NO'
                break
            else:
                stack.pop()
    if stack:
        answer = 'NO'

    print(answer)