import sys

sys.stdin = open("16478_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    s = input()

    size = 1000
    stack = [0] * size
    top = -1  # 마지막으로 삽입한 원소의 위치
    # 스택을 이용해서 풀껀데

    # 일단 문자를 스택에 넣어 (맨 처음 글자는 넣음)
    top += 1
    stack[top] = s[0]
    # 두번째 글자부터는 내가 제일 최근에 넣었던 글자와 비교해서
    for i in range(1, len(s)):
        # 만약 같다면 스택에서 pop
        if top != -1 and stack[top] == s[i]:
            top -= 1
        # 다르다면 현재 글자를 스택에 push
        else:
            top += 1
            stack[top] = s[i]

    print(f"#{tc} {top + 1}")
