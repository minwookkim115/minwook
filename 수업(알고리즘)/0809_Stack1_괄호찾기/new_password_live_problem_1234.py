import sys

sys.stdin = open("1234_input.txt", "r")

T = 10

for tc in range(1, T + 1):
    N, string = map(str, input().split())

    size = int(N)  # N은 비밀번호의 길이
    stack = [0] * size  # 비밀번호의 길이 만큼 stack 준비
    top = -1  # top은 -1로 초기화

    # string의 첫글자 집어넣기
    top += 1
    stack[top] = string[0]

    # string의 두번째 글자 부터 검사
    for i in range(1, len(string)):
        # top이 -1이 아니고
        # stack의 제일 나중에 들어간 글자가 string의 i 번째와 같으면
        if top != -1 and stack[top] == string[i]:
            # top을 -1 로 줄임
            # i 번째 글자를 넣지도 않았고
            # top을 -1로 줄여버렸으니 둘다 없어짐
            top -= 1
        # stack의 제일 나중글자와 string의 i번째가 같으면
        else:
            top += 1  # top을 증가시키고
            stack[top] = string[i]  # top에 i번째 string 삽입

    # 결국 stack 안에서 top번째 까지가
    # 겹치는 숫자를 제외하고 넣은 진짜 비밀번호
    password = ""
    for i in range(top + 1):
        password += stack[i]

    print(f"#{tc} {password}")
