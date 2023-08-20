# 아래 함수를 수정하시오.
sum = 0

def add_numbers(a, b):
    global sum
    sum = a + b

    return print(f"{a}과 {b}를 인자로 넘긴 경우,\n{sum}")


add_numbers(3, 5)

#수정한 add_numbers() 함수를 호출하시오.