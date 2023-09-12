import sys

sys.stdin = open("1225_input.txt", "r")

T = 10

for tc in range(1, T + 1):
    t = int(input())
    nums = list(map(int, input().split()))

    N = 8  # 숫자 범위
    q = [0] * (N + 1)  # 원형큐 생성

    front = rear = 0  # 머리와 꼬리는 0으로

    # 원형큐에 숫자 넣기
    for i in range(N):
        rear = (rear + 1) % N
        q[rear] = nums[i]

    # 뺄 숫자
    minus = 1

    while True:
        front = (front + 1) % N
        item = q[front]  # front로 뽑아서

        item -= minus  # 숫자 빼주기

        # 끝날 때
        if item <= 0:  # 0보다 작으면
            item = 0  # 0으로 만들고
            # 꼬리에 삽입
            rear = (rear + 1) % N
            q[rear] = item
            break
        # 0이 안되면 계속 반복
        else:
            rear = (rear + 1) % N
            q[rear] = item  # 꼬리에 그냥 item 삽입

            minus += 1  # 뺄숫자 1씩 더해주는데
            if minus > 5:  # 5보다 커지면
                minus = 1  # 다시 1로

    print(f"#{tc}", end=" ")

    for i in range(8):
        front = (front + 1) % N
        print(q[front], end=" ")
    print()
