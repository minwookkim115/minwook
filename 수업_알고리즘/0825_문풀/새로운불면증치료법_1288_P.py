import sys

sys.stdin = open("1288_input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    count = [0] * 10  # 1부터 9까지 다 봤는지 세기

    answer = 0  # N을 몇번곱해진 것 까지 봐야하는지

    a = 1
    while True:
        if answer != 0:  # 답이 0이 아니면
            break  # while 끝내기

        # 곱할때마다 본 숫자 리스트
        num_list = []
        for i in str(N * a):
            num_list.append(int(i))

        # 다음 곱하기 진행
        a += 1

        # 본숫자들 count인덱스에 + 1
        for i in num_list:
            count[i] += 1

        # count에 0이 없으면
        # 다 봤으면
        if 0 not in count:
            answer = N * (a - 1)  # 정답 구하고
            a = 1  # 초기화
            break

    print(f"#{tc} {answer}")
