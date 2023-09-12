class Person:
    def __init__ (self, name):
        self.name = name

    def greeting(self):
        return f"안녕, {self.name}입니다."
    

class Mom(Person):
    gene = "XX"

    def __init__ (self, name):
        super().__init__(name)
    
    def swim(self):
        return "엄마가 수영"


class Dad(Person):
    gene = "XY"

    def __init__ (self, name, age):
        super().__init__(name)
        self.age = age

    def walk(self):
        return "아빠가 걷기"


class FirstChild(Mom, Dad):
    dad_gene = Dad.gene

    def __init__ (self, name, age):
        super().__init__(name) # super는 유연하다 / 자기 알아서 찾아줌
        Dad.__init__(self, name, age) # Dad에 age가 있을땐 이렇게 따로 써야함

    def swim(self):
        return "첫째가 수영"

    def cry(self):
        return "첫째가 응애"

    


baby1 = FirstChild("아가")
print(baby1.cry())  # 첫째가 응애
print(baby1.swim()) # 첫째가 수영 / 본인의 인스턴스 메서드기 때문에 자기꺼 출력
print(baby1.walk()) # 아빠가 걷기 / 부모클래스 Dad에 있는거
print(baby1.gene) # XX

print(FirstChild.mro())
# [<class '__main__.FirstChild'>, <class '__main__.Mom'>, <class '__main__.Dad'>, <class '__main__.Person'>, <class 'object'>]
# △ 속성이건 메서드건 찾아 올라가는 순서
# print(baby1.dad_gene) # XY