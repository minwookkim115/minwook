############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def calc_average(speed_list):

    sum_speed = 0
    speed_count = 0

    for i in speed_list:
        sum_speed += i

    for i in speed_list:
        speed_count += 1
    
    return sum_speed / speed_count

    # count = 0
    # total = 0

    # for speed in speed_list:
    #     count += 1
    #     total += speed

    # avg = total / count

    # return avg



# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(calc_average([119, 124, 178, 192,]))  #=> 153.25
    
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    