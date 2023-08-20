############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def sum_digits(number):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    answer = []
    for i in str(number):
        answer.append(i)
    # 앞 자리 저장
    a = int(answer.pop(0))
    # 일의 자리수만 남은 경우 그대로 반환
    if answer == []:
        return a
    # 두 자리수 이상 남은 경우 앞 자리 + 뒤자리 재귀함수
    if answer != []:
        b = int(''.join(answer))
        return a + sum_digits(b)
    
    
# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(sum_digits(123))  # => 6
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.