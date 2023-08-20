############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def change_pwd(word, secret_code):

    password_list = []

    for i in list(word):
        password_list.append(str(secret_code[i]))

    password = "".join(password_list)

    return password
    
    # result = ""

    # for w in word:
    #     result += str(secret_code[w])

    # return result
    

# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    secret_code = {
        'a': 3,    'b': 8,    'c': 0,    'd': 1,
        'e': 7,    'f': 6,    'g': 7,    'h': 1,
        'i': 2,    'j': 5,    'k': 3,    'l': 6,
        'm': 5,    'n': 0,    'o': 7,    'p': 9,
        'q': 8,    'r': 2,    's': 4,    't': 9,
        'u': 6,    'v': 3,    'w': 2,    'x': 4,
        'y': 8,    'z': 1,    ' ': 0,
    }
    print(change_pwd('ssafy', secret_code)) # => 44368
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    