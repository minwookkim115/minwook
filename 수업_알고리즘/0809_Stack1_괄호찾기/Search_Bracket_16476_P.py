import sys

sys.stdin = open("16476_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    string = input()

    stack = []

    answer = 1

    for i in string:

        if i == "(" or i == "{" or i == "[":
            stack.append(i)

        if i == ")" or i == "}" or i == "]":
            if len(stack) == 0:
                answer = 0
                break

            a = stack.pop()
            if a == "(":
                if i != ")":
                    answer = 0
                    break
            elif a == "{":
                if i != "}":
                    answer = 0
                    break
            elif a == "[":
                if i != "]":
                    answer = 0
                    break

    if len(stack) != 0:
        answer = 0

    print(f"#{tc} {answer}")
