############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def sum_digits(number):
    
    # sum_digit = 0

    # for i in list(str(number)):
    #     if number // 10 == 0:
    #         return "n"
    #     else:
    #         sum_digit += int(i)
    
    
    # return sum_digit
    
    # 1. 재귀함수의 종료조건 설정
    if number < 10:
        return number # 10보다 작으면 10으로 나눈 나머지 == 나랑 같다
    
    # 2. 재귀 호출
    else:
        # 10으로 나눈 나머지를 구하면 각 자리수를 떼어낼수 있다.
        # 몫이 있어야 다음 자리수를 구할 수 있다.
        # 몫 ==> 다음 함수에서 나눌 수
        # 다음함수 ==> 재귀호출
        current_digit = number % 10 # 현재 자리수 curren_digit
        next_num = number // 10 # 다음에 나눌 수를 재귀 호출의 인자로 사용

        # 재귀호출의 결과를 어떤식으로 return 해줄 건지?
        # 결국에는 자리수의 누적 합
        # 현재 자리수 + 나머지 자리수

        return current_digit + sum_digits(next_num)


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(sum_digits(123))  # => 6
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    