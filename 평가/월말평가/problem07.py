############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def sum_primes(number):

    # prime_sum = 0

    # num_list = []

    # for i in range(4, 100):
    #     if i % 3 == 0:
    #         num_list.append(i)
    # for i in range(6, 100):
    #     if i % 5 == 0:
    #         num_list.append(i)
    # for i in range(8, 100):
    #     if i % 7 == 0:
    #         num_list.append(i)

    # num_list1 = []

    # for i in range(2, 100):
    #     if i % 2 == 1:
    #         num_list1.append(i)

    # prime_list = [2]

    # for i in num_list1:
    #     if i not in num_list:
    #         prime_list.append(i)

    # for i in prime_list:
    #     if i < number:
    #         if i == 17:
    #             continue
    #         prime_sum += i

    # return prime_sum

    # 소수인지 확인하려면 number - 1 까지 나눠보면 된다.
    result = 0

    # 2부터 numbe - 1  까지 나눠 봤는데 나머지가 0인 적이 있다. => 소수아님
    # 0인적이 없었으면 소수 합을 구한다. (17 제외)
    for num in range(2, number):
        is_prime = True # 소수라고 가정 후 시작

        if num == 17: # 17은 제외
            continue

        for i in range(2, num): # 나누어 떨어지는지 확인
            if num % i == 0:
                # 약수 i를 발견함
                is_prime = False # num은 소수가 아니라고 체크
                break
        
        if is_prime: # is_prime 이 처음 가정 그대로 소수인 경우만 합 구함
            result += num

    return result

# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(sum_primes(22)) # => 60
    print(sum_primes(33)) # => 143
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    