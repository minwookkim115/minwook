import sys

sys.stdin = open("pascal_input.txt", "r")

# 재귀함수를 반복문처럼 생각하지 마라 그랬는데
T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    num_list = []  # 비교할 문자열 리스트

    for i in range(1, N + 1):

        if i == 1:  # n이 1인 경우
            num_list.append(1)  # num_list 에 1을 추가
            print(f"#{tc}")
            print(1)  # 1 출력

        if i == 2:  # n이 2인 경우
            num_list.append(1)  # num_list 에 1을 추가
            print(1, 1)  # 1 1 출력

        if i >= 3:  # i가 3부터 N 까지
            new_num_list = [1]  # 1을 가지고 있는 새로운 리스트 생성
            for j in range(1, i - 1):  # 1, i-1 까지 진행 하면서
                new_num_list.append(num_list[j - 1] + num_list[j])  # 새로운 리스트에 num_list에 있던 수를 더하면서 추가
            new_num_list.append(1)  # 새로운 리스트에 마지막 1 추가
            # a = " ".join(map(str, new_num_list))  # 문자열로 변경하여 1 2 1 / 1 3 3 1 형식으로
            print(*new_num_list)  # 간단하게 언패킹으로 출력
            num_list = new_num_list  # num_list를 new_num_list로 초기화
