import sys
sys.stdin = open("algo2_sample_in.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    card = list(map(str, input().split()))

    B_q = []  # B는 queue로 앞에서부터 뺌
    C_st = []  # C는 stack으로 뒤에서부터 뺌

    plus = 0  # 더하기의 개수로 보너스 숫자
    for i in card:  # 카드 돌때마다
        if i == "+":  # 더하기 만나면
            plus += 1  # 보너스 숫자 + 1
        else:  # 숫자면
            a = int(i) + plus  # 보너스 숫자 더하기
            if a % 2 == 1:  # 홀수면
                B_q.append(a)  # B에
            else:  # 짝수면
                C_st.append(a)  # C에

    answer = 0  # 김싸피가 M번째에 고른 답
    # 김싸피가 점수를 획득하지 못하는 경우는
    # B와 C모두 M번째로 고를 수가 없는 경우
    # if len(B_q) < M and len(C_st) < M:
    #     answer = 0
    # # 고를수 있는 경우
    # else:
    for i in range(M):  # M번 돌면서
        if len(B_q) == 0:  # 비어있으면
            B = 0  # 0으로 계산
        else:  # 아니면
            B = B_q.pop(0)  # B는 앞에서 꺼냄
        if len(C_st) == 0:  # 비어 있으면
            C = 0  # 0으로 계산
        else:  # 아니면
            C = C_st.pop()  # C는 뒤에서 꺼냄

        answer = B + C  # M번째에 나올 답

    print(f"#{tc} {answer}")
