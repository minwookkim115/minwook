import sys

sys.stdin = open("algo2_sample_in.txt")


def check(line):  # 괄호 검사
    stack = [0] * 100
    top = -1

    # 한글자씩 분리해서 괄호 검사
    for c in line:
        # 떼온 글자가 여는 괄호이면 push
        if c in ["(", "{"]:
            top += 1
            stack[top] = c
        # 떼온 글자가 닫는 괄호이면
        elif c == ")":
            # 스택이 비어있는지 확인
            # 스택안에서 꺼내 와서 괄호 짝 비교
            if top >= 0 and stack[top] == "(":
                top -= 1
            else:
                return 0

        elif c == "}":
            # 스택이 비어있는지 확인
            # 스택안에서 꺼내 와서 괄호 짝 비교
            if top >= 0 and stack[top] == "{":
                top -= 1
            else:
                return 0

    # 스택의 크기가 0이 아니면 여는 괄호가 더 많다.
    if top >= 0:
        return 0

    return 1


def op(line):  # 괄호가 정상인 수식을 계산하여 결과를 얻는 함수
    stack = [0] * 100
    top = -1

    # 한글자씩 분리
    for c in line:
        # 닫는 괄호가 나올때까지 stack에 push
        # 닫는 괄호가 나오면 그때 계산을 시작하면 된다.
        if c not in [")", "}"]:
            top += 1
            stack[top] = c
        # 닫는 괄호가 나오면 계산 시작
        elif c == ")":  # 여는 괄호가 나올때 까지 스택에서 꺼내서 더하기
            res = 0  # 이 괄호에서의 계산 결과

            # 스택에 더할 숫자가 남아있고, 맨위 원소가 여는 괄호가 아니면 더하기
            while top > -1 and stack[top] != "(":
                res += int(stack[top])
                top -= 1

            # while문이 끝났으면 아직 여는괄호가 스택에 하나 남아있으니까
            # 제거
            top -= 1  # 여는괄호 pop

            # 계산 결과를 나중에 다른 괄호에서 쓰기 위해서 stack에 push
            top += 1
            stack[top] = res

        elif c == "}":
            res = 1  # 이 괄호에서의 계산 결과

            # 스택에 더할 숫자가 남아있고, 맨위 원소가 여는 괄호가 아니면 더하기
            while top > -1 and stack[top] != "{":
                res *= int(stack[top])
                top -= 1

            # while문이 끝났으면 아직 여는괄호가 스택에 하나 남아있으니까
            # 제거
            top -= 1  # 여는괄호 pop

            # 계산 결과를 나중에 다른 괄호에서 쓰기 위해서 stack에 push
            top += 1
            stack[top] = res
    # 괄호 밖에 숫자가 있는 경우
    if top != 0:
        return -1
    # 반복이 다 끝나고 나면 스택에 최종 계산 결과가 남아있다.
    return stack[top]


T = int(input())

for tc in range(1, T + 1):
    line = input()
    # 식의 계산 결과
    answer = - 1

    # 1. 괄호 검사
    if check(line) == 1:
        # 2. 식 계산
        answer = op(line)

    print(f"#{tc} {answer}")
