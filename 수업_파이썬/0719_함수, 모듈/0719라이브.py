def greeting(name, age):
    print(f"안녕, {name}, {age}!!")


greeting("Ailce", 25) # 안녕, Alice, 25!!

greeting(25, "Alice") # 안녕, 25, Alice!!

# 키워드 인자
greeting(age=25, name="Alice") # 안녕, Alice, 25!!

# positional argument follows keyword argument
# greeting(age=25, "Dave")

# 임의의 인자 목록
print("hi", "aaa", "bbb", "ccc")
print("hi", "aaa", "bbb")

def calculate_sum(*args):
    print(args) # (1, 2, 3, 4, 5) => tuple, 개수에 상관 없음

calculate_sum(1, 2, 3, 4, 5)



def calculate_sum(**kwargs):
    print(kwargs) # {'name': 'Alice', 'age': 30, 'address': 'korea'}

calculate_sum(name="Alice", age=30, address="korea")



print("hello", end=" ")
print("asdasd")
# hello asdasd



# 함수는 코드 내부에 local scope를 생성
num = 100

def my_func():
    print(num)

my_func()



print(sum([1, 2, 3])) # 6

sum = 10

print(sum) # 10

print(sum([1, 2, 3])) # print(10([1, 2, 3])) 이 되버림
# TypeError: 'int' object is not callable