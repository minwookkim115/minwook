while True:
    string = input()
    stack = []

    if string == '.':
        break

    if string == '(' or string == '[':
        stack.append(string)

    if string == ')':
        if stack[-1] == '(':
            stack.pop()
        else:
            print('no')
            break

    if string == ']':
        if stack[-1] == '[':
            stack.pop()
        else:
            print('no')
            break

    if stack:
        print('no')
    else:
        print('yes')
