import sys

stack = []

N = int(input())

for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == '1':
        stack.append(order[1])
    elif order[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order[0] == '3':
        print(len(stack))
    elif order[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    elif order[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)

# 9
# 4
# 1 3
# 1 5
# 3
# 2
# 5
# 2
# 2
# 5
