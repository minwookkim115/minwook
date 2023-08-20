icp = {"+": 1, "/": 2, "*": 2}
isp = {"+": 1, "/": 2, "*": 2}


def get_postfix(infix, n):
    postfix = ""  # 결과로 출력할 후위 표기식
    stack = []

    for i in range(n):

        if infix[i] not in "(+-/*)":

            postfix += infix[i]

        else:
            while stack and isp[stack[-1]] >= icp[infix[i]]:
                postfix += stack.pop()

            stack.append(infix[i])

    while stack:
        postfix += stack.pop()

    return postfix


string = "9+8+5+9+2+4+1+8+3+9+3+8+7+8+6+8+9+4+1+1+7+6+1+5+8+7+6+9+6+3+1+3+1+7+5+9+2+8+4+3+7+3+4+7+3+4+8+3+2+6+6"
n = 101
postfix = get_postfix(string, n)
print(postfix)