############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def make_answer(security_str, security_code):

    str_list = []

    for i in security_code:
        str_list.append(security_str[i])
    
    string = "".join(str_list)

    return string
    
    # result = ""

    # for code in security_code:
    #     result += security_str[code]

    # return result

# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    answer = make_answer('kXeFSOo1spkSMsuuoAiklFeqYz', [4,11,17,21,24])
    print(answer)   # => SSAFY
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    