def enQ(data):
    global rear
    global front
    if (front + 1) % cQsize == front:
        front = (front + 1) % cQsize
    rear = (rear + 1) % cQsize
    cQ[rear] = data


def deQ():
    global front
    front = (front + 1) % cQsize
    return cQ[front] 


cQsize = 4
cQ = [0] * cQsize
front = 0
rear = 0

enQ(1)
enQ(2)
enQ(3)
# print(deQ())
# print(deQ())
enQ(4)
enQ(5)
print(cQ)
print(deQ())
print(deQ())
print(deQ())