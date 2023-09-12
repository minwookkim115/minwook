arr = [10, 6, 4, 5, 1, 3, 2, 9, 7, 8]  # 힙에다가 넣을 것

# 최대 힙
heap = [0] * 11
# 마지막에 넣은 원소 위치를 비교할
last = 0


# 삽입 연산
def enq(item):
    global last
    last += 1  # 마지막 위치에 원소 추가
    heap[last] = item

    # 원소를 추가하고나서 (부모노드 > 자식노드) 이 조건을 만족하도록 해야한다.
    # 현재 위치를 자식 노드로 생각
    # 부모노드의 위치를 계산 (2로 나누면 계산 가능)
    c = last
    p = c // 2
    # 부모노드가 존재하고, 자식노드가 부모노드보다 작을 때 까지 위치를 바꾼다.
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        # 그 위의 부모랑도 비교
        # 자식과 부모의 위치를 그 위로 바꾸고 계속 비교 이어나가기
        c = p
        p = c // 2


# 삭제 연산
def deq():
    global last

    # 루트노드를 삭제할껀데 이따가 자리 바꿀거니까 미리 지정
    temp = heap[1]

    # 마지막 노드를 루트위치에 땡겨온다
    heap[1] = heap[last]

    # 원소하나 삭제 했으니까 마지막 원소 인덱스 -1
    last -= 1

    # 루트부터 자리를 찾아가기 시작
    p = 1
    c = p * 2  # 일단 왼쪽 자식부터 비교 (완전 이진 트리)

    # 자리 조정
    # 최대 힙은 부모가 자식보다 크다
    # 부모가 자식보다 작으면 계속 자리를 교환

    # 왼쪽자식의 인덱스가 last보다 작아야 트리 안에 존재 하는 것이다.
    while c <= last:
        # 왼쪽 자식이 있으면 오른쪽 자식도 있나 확인
        # 부모 > 자식
        if c + 1 <= last and heap[c] < heap[c + 1]:
            # 오른쪽 자식이 있고 오른쪽 자식이 왼쪽 자식보다 크다.
            # 비교 대상을 오른쪽 자식으로 변경
            c = c + 1

        if heap[p] < heap[c]:
            # 자식이 더크면 자리를 교환
            heap[p], heap[c] = heap[c], heap[p]
            p = c  # 자식을 새로운 부모로 생각
            c = c * 2  # 왼쪽 자식을 기준으로 비교 계속 하기
        else:
            # 그 밑에는 어차피 나보다 작은애들만 있으니까
            # 내 자리를 찾았다. 반복 중단
            break

    # 루트 노드 return
    return temp


for i in range(10):
    enq(arr[i])

print(heap)

sorted_arr = []
for i in range(10):
    sorted_arr.append(deq())

print(sorted_arr)