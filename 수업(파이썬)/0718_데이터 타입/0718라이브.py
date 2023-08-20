# 파이썬 실핼할 때 bash 에서 python 0718.py 로 할수 있도록
# 진법 변경(10진수 - n진수)
print(bin(12)) # 1100
print(oct(12)) # 14
print(hex(12)) # c

print(2 / 3)

print(5 / 3)

# 지수(제곱하는 횟수 표현 10^)

print(314e-2) # 3.14
print(314e2) # 31400.0

print('이 다음엔 엔터\n입니다.')

# f-string => intepolation
bugs = "roaches"
counts = 100
area = "living room"
print(f"Debuugging {bugs} {counts} {area}")
print("Debuugging {} {} {}".format(bugs, counts, area)) # f-string 이전의 방법
print("Debuugging %s %d %s" % (bugs, counts, area)) # 옛날 방법

# f-string 응용
greeting = "hi"
print(f"{greeting:^10}") # 열칸중에 가운데 둔다(^10)
print(f"{greeting:>10}") # 열칸중에 오른쪽에 둔다(>10)
print(f"{3.141592:.4f}") # 실수를 소수점 네자리 까지 출력한다(.4f)

# 5. 컬렉션
# 불변과 가변의 차이
my_str= "hello"
# TypeError : 'str' object does not support item assignment
# my_str[0] = "z"

my_list = [1, 2, 3]
my_list[0] = 100
print(my_list) # [100, 2, 3]

list_1 = [1, 2, 3]
list_2  = list_1

list_1[0] = 100
print(list_1) # [100, 2, 3]
print(list_2) # [100, 2, 3]

x = 10
y = x

x = 20
print(x) # 20
print(y) # 10