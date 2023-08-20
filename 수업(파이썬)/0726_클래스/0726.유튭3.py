class Circle():
    pi = 3.14

    def __init__(self, r):
        self.r = r

c1 = Circle(5)
c2 = Circle(10)

print(Circle.pi) # 3.14
print(c1.pi) # 3.14 => class의 pi가 아니라 c1에 pi라는 인스턴스를 생성
print(c2.pi)

Circle.pi = 5 # 클래스 변수 생성
print(Circle.pi)
print(c1.pi)
print(c2.pi)

c2.pi = 5 # 인스턴스 변수 변경
print(Circle.pi)