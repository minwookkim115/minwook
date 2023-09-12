# 스택을 사용 (파이썬의 메소드)

stack = []  # 파이썬에서는 크기 정할필요 없음


# stack.append(item) => push
# if stack > 0:
# stack.pop() = > pop

def py_push(item):
    stack.append(item)


def py_pop():
    if len(stack) == 0:
        # 언더플로우 발생 / 원소 삭제 불가
        return
    else:
        return stack.pop()  # 실제로 삭제


for i in range(10):
    py_push(i)

print(stack)

for i in range(10):
    print(py_pop(), end=" ")

print()
print(stack)

print("===================================")

# 스택 사용 (인덱스)
# 원소 자체를 삭제하지는 않음
# 인덱스만 의미가 있다.
top = - 1
size = 10
stack = [0] * size


def my_push(item):
    global top
    top += 1
    if top == size:
        print("오버플로우")
    else:
        stack[top] = item


# 그냥 return 만 하는거지 직접 삭제하지는 않음
def my_pop():
    global top
    if top == -1:
        print("언더플로우")
        return
    else:
        top -= 1
        return stack[top + 1]


def peek():
    # top 이 -1 이면 원소가 없다
    if top > -1:
        return stack[top]


for i in range(10):
    my_push(i)

print(stack)

for i in range(10):
    print(my_pop(), end=" ")

print()
print(stack, top)

my_push(100)

print(stack, top)
