# 클래스 정의 / 클래스는 파스칼 케이스를 사용 not 스네이크 케이스
class Person:
    # 속성(변수)
    # ▽ 클래스 변수 / 클래스 내부에 선언된 변수
    # ▽ 클래스로 생성된 모든 인스턴스들이 공유하는 변수
    blood_color = "red"

    # 메서드 / 생성자 함수
    # __ __개발자가 직접 호출하지 않음 자연스럽게 동작
    # init = 초기화
    def __init__(self, name): # self는 자기자신 = singer1, singer2
        # ▽ 인스턴스 변수 / 인스턴스(객체)마다 별도로 유지되는 변수
        # ▽ 독립적인 값을 가지고 인스턴스가 생성될 때마다 ★초기화★됨
        self.name = name  # 생성자 메서드 / 인스턴스를 생성할 때 자동호출

    # ▽ 인스턴스 메서드 / 각각의 인스턴스에서 
    def singing(self):
        return f"{self.name}가 노래합니다."
    
# 인스턴스 생성
# singer1(인스턴스) Person(클래스)
singer1 = Person("iu")
singer2 = Person("BTS") # Person이라는 똑같은 클래스로 만든 다른 인스턴스

# 메서드 호출
print(singer1.singing()) # iu가 노래합니다.
print(singer2.singing()) # BTS가 노래합니다.

# 속성(변수) 사용
print(singer1.blood_color) # red
print(singer2.blood_color) # red