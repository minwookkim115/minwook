import sys

sys.stdin = open("16638_input.txt", "r")


# 큐에 삽입하는 함수
def enqueue(item):
    global rear
    rear += 1
    q[rear] = item


# 큐의 앞쪽에서 꺼내는 함수
def dequeue():
    global front
    front += 1
    return enqueue(q[front])  # 꺼낸것을 큐에 삽입


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # N의 최대값이 100 / M의 최대값이 100 이므로
    # 가장 커질 수 있는 1100 만큼 q 생성
    q = [0] * 1100

    # arr을 q에 삽입
    for i in range(len(arr)):
        q[i] = arr[i]

    # q에서 제거해야할 부분 초기화
    front = -1
    # q에서 삽입해야할 부분 초기화
    rear = N - 1

    # front가 M만큼 진행해야 하고
    # N -1 만큼의 arr이 q에 들어가 있으므로
    # front가 N + M이 될때까지
    while front < M + N:
        # 삭제하고 추가하는 함수 실행
        dequeue()

    print(f"#{tc} {q[front]}")
