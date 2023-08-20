import sys

sys.stdin = open("1223_input.txt", "r")

# 연산자 우선순위
first = {"+": 1, "*": 2}


# 후위계산식 구하는 함수
def get_postfix(infix, n):
    postfix = ""
    stack = []

    for i in range(n):
        if infix[i] not in "+*":  # +, * 가 아니면
            postfix += infix[i]  # postfix에 넣고

        # 정수면
        else:
            # 스택이 비어있지 않고, 스택안에 들어간 마지막 연산자 우선순위가 더 높으면
            while stack and first[stack[-1]] >= first[infix[i]]:
                postfix += stack.pop()  # 우선순위가 더 높으니까 pop해서 postfix에
            stack.append(infix[i])  # 아니면 stack에 append

    # stack이 빌때까지 pop
    while stack:
        postfix += stack.pop()

    return postfix


# 후위계산식 계산하는 함수
def get_result(post):
    stack = []

    for i in post:
        if i not in "+*":  # postfix에 +, * 가 아니면
            stack.append(int(i))  # stack에 정수형태로 append

        # +, * 면
        else:
            # 스택에서 pop해서
            right = stack.pop()
            left = stack.pop()

            if i == "+":  # + 면 더하고
                result = left + right
            if i == "*":  # * 면 곱하고
                result = left * right

            # 계속 계산을 위해 result append
            stack.append(result)

    # 마지막 계산을 pop
    return stack.pop()


T = 10

for tc in range(1, T + 1):
    N = int(input())
    num = input()

    postfix = get_postfix(num, N)
    result = get_result(postfix)
    print(f"#{tc} {result}")
