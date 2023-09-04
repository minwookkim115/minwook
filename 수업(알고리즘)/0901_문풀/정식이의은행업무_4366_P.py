import sys

sys.stdin = open("4366_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):

    A = input()  # 2진수
    B = list(map(int, input()))  # 3진수

    N = len(A)  # 2진수 길이
    M = len(B)  # 3진수 길이
    answer = 0

    binary = int(A, 2)  # 2진수를 10진수로
    # 하나씩 바꾼 숫자 리스트
    bin_list = [0] * N
    for i in range(N):
        bin_list[i] = binary ^ (1 << i)

    for i in range(M):
        num1 = 0
        num2 = 0
        for j in range(M):
            # 3진수 중 변하지않는 고정값
            if i != j:
                num1 = num1 * 3 + B[j]
                num2 = num2 * 3 + B[j]
            # 3진수 숫자중 0 1 2 로 변하는 숫자
            else:
                num1 = num1 * 3 + (B[j] + 1) % 3
                num2 = num2 * 3 + (B[j] + 2) % 3
        if num1 in bin_list:
            answer = num1
            break  # for i
        if num2 in bin_list:
            answer = num2
            break

    print(f"#{tc} {answer}")
