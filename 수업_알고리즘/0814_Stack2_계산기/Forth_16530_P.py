import sys

sys.stdin = open("16530_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    string = input().split()
    string.pop()    # '.'을 지워 버리고
    stack = []  # 빈 stack

    for i in string:
        if i not in "+-/*": # 연산자 아니면
            stack.append(int(i))    # stack에 append
        else:
            if len(stack) < 2:  # 연산자는 기본적으로 2개의 숫자가 필요한데 숫자가 2개보다 적으면
                stack.clear()
                stack.append("error")   # error 넣어버리고
                break   # 끝
            # 다시 진행
            # 숫자 두개 pop()
            right = stack.pop()
            left = stack.pop()

            # 연산 실행
            if i == "+":
                result = left + right
            if i == "-":
                result = left - right
            if i == "/":
                result = left // right
            if i == "*":
                result = left * right

            stack.append(result)    # 다음 연산에 필요하니까 result를 다시 append

    # 계산이 끝났을 때 stack에 숫자 두개 이상 있으면
    # 연산자의 개수 부족으로 error
    if len(stack) >= 2:
        stack.clear()
        stack.append("error")

    print(f"#{tc} {stack.pop()}")
