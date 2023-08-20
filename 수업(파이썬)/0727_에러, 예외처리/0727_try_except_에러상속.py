try:
    num = int(input("100으로 나눌 값을 입력해 : "))
    print(100 / num)
except BaseException:
    print("숫자를 입력하라고")
except ZeroDivisionError:
    print("왜 0을 입력하는거야??") # 실행되지 않음
except:
    print("에러가 발생했어")

# ZeroDivisionError는 BaseException의 하위클래스
