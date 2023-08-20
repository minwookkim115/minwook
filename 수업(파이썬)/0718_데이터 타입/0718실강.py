# a 를 10번 증가시키는데 1씩 증가 시키고 싶다

a = 0
for i in range(10):
    a += 1
    # a = a + 1

print(a)


a = 10
b = 10

print(a == b) # True
print(a != b) # False

print(a is b) # True

a1 = [1, 2, 3]
b1 = [1, 2, 3]

print(a1 == b1) # True
print(a1 is b1) # False => 값은 같지만 메모리 참조하는 곳이 달라서 False

a2 = [1, 2, 3]
b2 = a2

print(a2 is b2) # True

print(True and True) # True
print(True and False) # False
print(False and False) # False

print(5 == 5 and True) # True
print(5 == 1 and True) # False

print(5 == 1 or True) # True
print(False or False) # False

print(not True) # False
print(not False) # True
print(not (5 == 1)) # True

print(5 == 4 and 1 == 1) # 이미 앞이 False기 때문에 뒤에는 평가 안함

print(3 and 5) # 5
print(3 and 0) # 0
print(0 and 3) # 0
print(0 and 0) # 0

print(5 or 3) # 5
print(3 or 0) # 3
print(0 or 3) # 3
print(0 or 0) # 0

# 형변환
ls = [1, 2, 3]

print(tuple(ls)) # (1, 2, 3)

dic = {"name": "minuk", "height": 171}

print(list(dic)) # ["name", "height"] key만 추출