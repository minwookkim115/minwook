class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"안녕, {self.name}입니다.")
    

class Professor(Person):
    def __init__ (self, name, age, department):
        # Person.__init__(self, name, age) # Person에서 __init__ 함수 가져옴
        # super = Person, 다중상속때 super가 모든 부모클래스를 가르킴
        super().__init__(name, age)
        self.department = department


class Student(Person):
    def __init__ (self, name, age, gpa):
        # Person.__init__(self, name, age) # Person에서 __init__ 함수 가져옴
        super().__init__(name, age)
        self.gpa = gpa

p1 = Professor("박교수", 49, "컴공")
s1 = Student("김학생", 20, 3.5)

p1.talk()
s1.talk()
