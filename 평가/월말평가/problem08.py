############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def calculate_sum_number(word):
    pass
    # check_isdigit_list = []

    # for i in list(word):
    #     check_isdigit_list.append(i.isdigit())

    # True_index_list = []

    # for i in check_isdigit_list:
    #     if i == True:
    #         True_index_list.append(check_isdigit_list.index(i))

    # return True_index_list

    total = 0

    for char in word:
        if char.isdigit() == True:
            total += int(char) # char 는 문자열이니까 정수로 바꿈

    return total


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(calculate_sum_number('ab123cd45ef6')) # => 21
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.