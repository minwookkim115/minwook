num = 10 # 전역 변수 => global의 num

def my_func():
    num = 20 # my_func 안에 num
    print("함수 실행 : num을 20으로 바꿨다.")

my_func()

print(num) # 10



num = 10 # 전역 변수 => global의 num

def my_func():
    global num
    num = 20
    # global에 num을 20으로 바꿈
    print("함수 실행 : num을 20으로 바꿨다.")

my_func()

print(num) # 20

numbers = [1, 2, 3]

def hello():
    numbers[0] = 4

hello()
print(numbers)