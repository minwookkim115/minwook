import sys

sys.stdin = open("16719_input.txt", "r")

# enq하기
def enq(item):
    global last
    # last 1 씩 올리면서
    last += 1
    # 일단 힙에 넣고
    heap[last] = item

    # 자식노드
    c = last
    # 부모 노드
    p = c // 2

    # 부모노드가 있고, 부모노드가 자식노드보다 크면
    while p and heap[p] > heap[c]:
        # 자리 바꾸기
        heap[p], heap[c] = heap[c], heap[p]

        # c를 p로 바꾸고
        # 그 위에랑도 계속 비교
        c = p
        p = c // 2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 노드의 개수
    arr = list(map(int, input().split()))  # 노드에 들어갈 수

    last = 0 # 입력할 곳
    heap = [0] * (N + 1) # 힙 생성

    # 힙에 enq 하기
    for i in range(N):
        enq(arr[i])

    # 조상 노드에 저장된 거 더해야 하니까
    # 자기자신 빼고
    answer = -heap[last]
    # last가 1이 될때 까지
    while last > 0:
        # answer에 last더하면서
        answer += heap[last]
        # 조상 노드로
        last = last // 2

    print(f"#{tc} {answer}")
