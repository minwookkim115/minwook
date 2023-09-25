import sys

sys.stdin = open("algo1_sample_in.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    arr = []
    for _ in range(3):
        a = input()
        arr.append(a)

    # N = 자릿수
    # P = 16진수
    # Key = exclusive or로 비교할 key
    N = int(arr[0])
    P = arr[1]
    Key = arr[2]

    # 16진수를 리스트로 만들고
    P_l = []
    for i in P:
        P_l.append(i)

    # 16진수의 한 글자는 2진수의 4자리 이므로
    # 체크할 비트를 만들어서
    # 비교할 key를 체크 비트에 넣기
    check_bit = [0] * 4
    for i in range(4):
        if int(Key, 16) & (1 << i):
            check_bit[i] = 1
    check_bit.reverse()

    # 정답
    answer = ""
    # 16진수를 돌면서
    for i in P_l:
        bit = [0] * 4  # 비트배열 하나 만들고
        num = int(i, 16)  # 10진수로 바꿔준 다음
        for j in range(4):
            if num & (1 << j):  # 2진수로 바꿔서
                bit[j] = 1  # 비트에 삽입
        bit.reverse()

        # exclusive or 한 값
        sub_answer = ""
        # key의 2진수 check비트와
        # 16진수의 한자리수 비트를 돌면서
        for k in range(4):
            if check_bit[k] != bit[k]:  # 다르면
                sub_answer += "1"  # 1
            else:  # 같으면
                sub_answer += "0"  # 0

        # 16진수로 바꿀 값
        ss_answer = 0
        # 2진수로 바꾼 값 돌면서
        for l in range(3, -1, -1):
            # 1이면 10진수로 바꾸기
            if sub_answer[l] == '1':
                ss_answer += 2 ** abs(l - 3)

        # 16진수는 10부터 16까지 A ~ F로 표현
        if ss_answer < 10:
            answer += str(ss_answer)
        elif ss_answer == 10:
            answer += 'A'
        elif ss_answer == 11:
            answer += 'B'
        elif ss_answer == 12:
            answer += 'C'
        elif ss_answer == 13:
            answer += 'D'
        elif ss_answer == 14:
            answer += 'E'
        elif ss_answer == 15:
            answer += 'F'

    # 정답 출력
    print(f"#{tc} {answer}")
