class Person:
    # 클래스 변수
    blood_color = "red"
        # 생성자 함수
    def __init__(self, name):
        self.name = name
    # grade는 더해줄 인자
    def hello(self, grade):
        print(f"안녕하세요 저는 {self.name} 이고 {grade} 학년 입니다.")

    


p1 = Person("minuk")
p2 = Person("gildong")

print(p1.name)
print(p2.name)

print(p1.blood_color)
print(p2.blood_color)

# p1의 인스턴스 변수 blood_color 가 만들어져 버림 / 파이썬 튜터 확인
p1.blood_color = "green"

# 클래스 변수에는 인스턴스로 접근하지 말고 가급적 클래스 이름으로 접근
print(p1.blood_color)
print(p2.blood_color)
print(Person.blood_color)

p1.hello(3)
p2.hello(4)


class MyClass:

    def __str__(self):
        return "나는 MyClass다."

c1 = MyClass()

print(c1)