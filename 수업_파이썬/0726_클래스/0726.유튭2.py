# Person 정의
class Person:
    # 클래스 속성, 클래스 변수
    name = "unknwon"

    # 인스턴스 메서드 => why 인스턴스가 사용하기 때문에
    def talk(self):
        print(self.name)

p1 = Person()
p1.talk() # unknwon / 인스턴스 변수가 없으면 클래스 안에서 찾음

# p2 인스턴스 변수 설정 전/후
 
p1.address = "korea"
print(p1.address) # korea
# p1 이라는 Person Instance에 address = 'korea'가 생성
# 인스턴스 변수는 알아서 지가 만들고 사용함
# 인스턴스 변수는 행동(메서드)은 들고 있을 수 없다.

# p2 = Person()
# p2.talk() # unknown

# p2.name = "Kim"
# p2.talk() # Kim

# print(Person.name) # unknown
# print(p1.name) # unknown
# print(p2.name) # Kim
