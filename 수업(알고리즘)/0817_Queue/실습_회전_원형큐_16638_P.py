import sys

sys.stdin = open("16638_input.txt", "r")


# 원형큐

# 엔큐 함수
def enqueue(item):
    global rear
    rear = (rear + 1) % N  # rear가 N보다 커질때 % N
    q[rear] = item  # q[rear]에 item 엔큐


# 디큐 함수
def dequeue():
    global front
    front = (front + 1) % N  # front가 N보다 커질때 % N
    return enqueue(q[front])  # front에서 디큐한 숫자를 바로 엔큐


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 원형큐 생성
    q = [0] * (N + 1)
    # rear와 front 초기화
    rear = front = 0

    # 빈 원형큐에 숫자 삽입
    for i in range(N):
        enqueue(arr[i])

    # M번 디큐하고 디큐한것을 바로 엔큐
    for _ in range(M):
        dequeue()

    # front한 위치 + 1이 제일 앞에오는 숫자
    print(f"#{tc} {q[(front + 1) % N]}")
