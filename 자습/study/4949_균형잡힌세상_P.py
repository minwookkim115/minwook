while True:
    string = input()
    stack = []
    answer = 'yes'

    if len(string) == 1:
        break

    for i in string:

        if i == '.':
            break

        if i == '(' or i == '[':
            stack.append(i)

        if i == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    answer = 'no'
                    break
            else:
                answer = 'no'
                break

        if i == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    answer = 'no'
                    break
            else:
                answer = 'no'
                break

    if stack:
        answer = 'no'

    print(answer)

