numbers = [1, 2, 3, 4, 5]

a, *b, c = numbers

print(a, b, c)

print(numbers)
print(*numbers)
# print(numbers[0], numbers[1] ... )

names = ["alice", "jane", "peter"]
print(*names)
print(names)

# **을 활용한 언패킹
def my_function(x, y, z):
    print(x, y, z)

my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict) # 1 2 3

# 세제곱 함수
# 입력받은 수를 세제곱하여 반환(return)하는 함수 cube() 만들어 보세요
def cube(x):
    return x ** 3

print(cube(2)) # 8
print(cube(10)) # 1000

# 사각형에 넓이를 구하는 함수
# rectangle(w, h)
def rectangle(w, h):
    return w * h

print(rectangle(20, 30))

# 사각형에 넓이, 둘래를 구하는 함수
# rectangle(w, h)
def rectangle(w, h):
    return (w * h, 2 * (w + h))

print(rectangle(20, 30))

