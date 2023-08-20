import sys

sys.stdin = open("pascal_input.txt", "r")

num_list = []  # 비교할 문자열 리스트
T = int(input())

for tc in range(1, T + 1):
    N = int(input())


    def pascal(n):
        # n에 1을 입력하고 n에 1을 더해가는 재귀함수를 사용하여
        # n이 입력값 N이 되면 종료
        if n == N + 1:
            return

        global num_list  # num_list 호출
        if n == 1:  # n이 1인 경우
            num_list.append(1)  # num_list에 1을 추가
            print(f"#{tc}")
            print(1)  # 1 출력
            pascal(n + 1)  # 재귀함수로 pascal(2)로 진행
        if n == 2:  # pascal(2) 함수로 n이 2가 되면
            num_list.append(1)  # num_list에 1을 추가
            print(1, 1)  # 1 1 출력
            pascal(n + 1)  # 재귀함수로 pascal(3)로 진행
        if n >= 3:  # pascal(3 ~ 10) 까지 진행
            new_num_list = [1]  # 1을 가지고 있는 새로운 리스트 생성
            for i in range(1, n - 1):  # 1, n-1 까지 진행 하면서
                new_num_list.append(num_list[i - 1] + num_list[i])  # 새로운 리스트에 num_list에 있던 수를 더하면서 추가
            new_num_list.append(1)  # 새로운 리스트에 마지막 1 추가
            a = " ".join(map(str, new_num_list))  # 문자열로 변경하여 1 2 1 / 1 3 3 1 형식으로
            print(a)  # 출력
            num_list = new_num_list  # num_list를 new_num_list로 바꾸고
            pascal(n + 1)  # 재귀함수로 pascal(10) 까지 진행


    pascal(1)
