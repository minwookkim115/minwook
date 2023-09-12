T = int(input())

for tc in range(1, T + 1):
    row = input()  # 괄호의 짝이 맞는지 검사할 문자열

    stack = []  # 스택

    answer = 1  # 1 이면 괄호과 제대로 되어있다, 0 이면 괄호가 제대로 안돼있다.

    # 괄호검사
    # row 에서 한글자씩 떼어 와서 검사
    for c in row:
        # 떼어낸 한 글자가 만약 여는 괄호면 => 스택에 삽입
        if c == "(":
            stack.append(c)

        # 떼어낸 글자가 닫는 괄호다 => 스택에서 꺼내와서
        # 짝이 맞는지 검사 => 괄호의 종류가 다르면 오류!
        # 꺼내오기 전에 스택이 비어있나 확인, 비어있으면 오류!
        if c == ")":
            if len(stack) == 0:
                answer = 0
                break

            b = stack.pop()
            if not(b == "(" and c == ")"):
                answer = 0
                break
    # 모든 검사가 끝난 후에 스택이 비어있지 않으면 오류!
    if len(stack) != 0:
        answer = 0

    print(f"#{tc} {answer}")
