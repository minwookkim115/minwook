import sys

sys.stdin = open("1222_input.txt", "r")


# 후위표기식으로 만드는 함수
def get_postfix(infix, n):
    postfix = ""  # 나타낼 후위표기식
    stack = []

    for i in range(n):  # 주어진 문자열의 길이만큼 돌면서
        if infix[i] != "+":  # 연산자가 + 뿐이므로 i가 연산자 +가 아니면(숫자이면)
            postfix += infix[i]  # 후위표기식에 입력
        # i가 + 일때
        else:
            if len(stack) >= 1:  # 스택에 1개 이상 +가 들어가 있으면
                postfix += stack.pop()  # +를 pop해서 후위표기식에 입력하고
            stack.append(infix[i])  # i를 stack에 append

    # 스택에 마지막 + 하나가 남으므로
    # 후위표기식에 + 입력
    postfix += "+"
    return postfix


# 후위표기식을 계산하는 함수
def get_result(post):
    stack = []

    for i in post:
        if i != "+":  # 연산자는 +뿐이므로 i가 연산자 +가 아닐 때
            stack.append(int(i))  # stack에 i를 정수로 append

        # i가 정수일 때
        else:
            # 4/3을 후위표기식으로 표기할 때 43/ 으로 표기
            # stack에 4 3 순서로 들어가 있으므로 3이먼저 나오고 4가 나옴
            # 오른쪽 왼쪽 구분 해줘야함
            right = stack.pop()  # stack에서 마지막으로 들어간 정수 pop
            left = stack.pop()  # stack에서 그다음으로 들어간 정수 pop

            # 연산자 +하나 뿐이므로 +만 수행
            result = right + left

            # 계속 더해가야 하므로 더한 값을 다시 stack에 append
            stack.append(result)

    # 수행이 끝나고 마지막 남은 stack을 pop
    return stack.pop()


T = 10

for tc in range(1, T + 1):
    N = int(input())
    sum_num = input()

    postfix = get_postfix(sum_num, N)

    print(f"#{tc} {get_result(postfix)}")
