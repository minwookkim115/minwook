############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def caesar(word, num):

    # word_num_list = []
    # for i in list(word):
    #     word_num_list.append(ord(i))


    # word_num_list1 = []
    # for i in word_num_list:
    #         word_num_list1.append(i + num)

    # word_num_list2 = []
    # for i in word_num_list1:
    #     if 97 <= i <= 122 or 65 <= i <= 90:
    #         word_num_list2.append(i)
    #     else:
    #         word_num_list2.append(i - 26)

    # word_list =[]

    # for i in word_num_list2:
    #     word_list.append(chr(i))

    # string = "".join(word_list)

    # return string

    result = ""

    for char in word:
        temp = ""
        # 대문자인 경우
        if char.isupper():
            # char 가 'A'랑 얼만큼 떨어져 있는가??
            # ord(char) - 65
            # char 가 'C' 라면 67, 'A' 랑은 2만큼 떨어져 있다.
            # 그래서 내가 이 char를 얼만큼 밀었는데? => num
            # ord(char) - 65 + num => 밀고나서 'A'랑 얼만큼 떨어져 있는지 알 수 있다.
            # num이 26보다 크면??
            # 29번 미는거랑 3번 미는거랑 똑같다. num % 26 만큼만 민다
            # (ord(char) - 65 + num) % 26 => 'A'랑 얼만큼 떨어져 있는지 구함
            # 다시 문자로 바꾸면 되는데 chr()
            # chr('A'의 숫자 + 'A'와 얼만큼 떨여져 있는지)
            # chr(65 + (ord(char) - 65 + num) % 26)
            temp = chr(65 + (ord(char) - 65 + num) % 26)
        # 소문자인 경우
        elif char.islower():
            temp = chr(97 + (ord(char) - 97 + num) % 26)

        result += temp

    return result
# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(caesar('ssafy', 1))   # => ttbgz
    print(caesar('Python', 10)) # => Zidryx
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    