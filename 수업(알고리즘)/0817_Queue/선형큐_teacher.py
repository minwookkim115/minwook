# 큐 초기화
size = 10
q = [0] * size
front = rear = -1


# 삽입 여산
def enqueue(item):
    global rear
    # 삽입을 하기 전에 큐가 가득 찼는지 확인
    if isFull():
        print("full")
        return
    rear += 1
    q[rear] = item


# 삭제연산
def dequeue():
    global front
    # 삭제하기 전에 큐가 비어있는지 확인
    if isEmpty():
        print("empty")
        return
    front += 1
    return q[front]


# 큐가 가득 찼는지
def isFull():
    return rear == size - 1


# 큐가 비어있는지
def isEmpty():
    return front == rear


for i in range(10):
    enqueue(i)

print(q)
print(isEmpty())  # False
print(isFull())  # True

for i in range(10):
    print(dequeue(), end=" ")
print()

print(q)
print(isEmpty())  # True / front랑 rear랑 같으니까
print(isFull())  # True / rear가 size-1 까지 갔으니까
