try:
    num = int(input("100으로 나눌 값을 입력해 : "))
    print(100 / num)
except ValueError:
    print("숫자를 입력하라고")
except ZeroDivisionError:
    print("왜 0을 입력하는거야??")
except:
    print("에러가 발생했어")

# 내장예외안에 에러가 클래스로 존재, so 에러내에 상속개념이 존재
# if ValueError 안에 ZeroDivisionError가 있다면 ZeroDivisionError는 절대안됨
# so 하위클래스들을 먼저 써야함
