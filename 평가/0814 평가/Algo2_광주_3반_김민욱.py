import sys
sys.stdin = open("algo2_sample_in.txt")

T = int(input())

for tc in range(1, T + 1):
    lst = list(input())

    stack = []
    answer = 0  # 괄호가 맞지 않는 경우

    for i in lst:
        if lst[0] != "(" and lst[0] != "{":  # 괄호에 둘러쌓이지 않는 숫자가 있는 경우
            answer = -1
            break

        if i == "(" or i == "{":  # 여는괄호가 나오면 stack에 append
            stack.append(i)

        if i == ")" or i == "}":  # 닫는 괄호가 나왔을 때
            if len(stack) == 0:  # 닫는 괄호가 제일 앞에 있으면
                answer = - 1
                break
            a = stack.pop()  # 닫는 괄호가 나왔을때 스택에서 pop
            if i == ")":  # 닫는 괄호일 때
                if a != "(":  # pop 한거랑 다르면
                    answer = -1
                    break

            if i == "}":  # 닫는 괄호일 때
                if a != "{":  # pop 한거랑 다르면
                    answer = -1
                    break

    if len(stack) != 0:  # 괄호의 짝이 맞지 않을 때
        answer = -1

    print(f"#{tc} {answer}")
