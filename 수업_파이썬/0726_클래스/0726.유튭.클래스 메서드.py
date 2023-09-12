class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1
    
    @classmethod
    def number_of_population(cls):
        print(f"인구수는 {cls.count}입니다.")

person1 = Person("iu")
person2 = Person("BTS")

Person.number_of_population() # 인구수는 2입니다.
# 클래스.number_of_population() 클래스가 호출 / 클래스 메서드