import sys

sys.stdin = open("4698_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    D, A, B = map(int, input().split())

    is_prime = [True for _ in range(B + 1)]  # 모두 소수라고 가정
    is_prime[0] = False
    is_prime[1] = False
    # 0 ~ B + 1 까지의 소수가 아닌 것은 False 로 변경
    for i in range(2, int(B ** 0.5) + 1):
        if is_prime[i]:
            j = 2
            while i * j <= B:
                is_prime[i * j] = False
                j += 1

    special_prime_count = 0
    for i in range(A, B + 1):  # A 부터 B 까지
        if is_prime[i]:  # 소수면 / True 는 생략
            prime = str(i)  # 문자열로 바꿔주고
            if str(D) in prime:  # D가 prime 에 있으면
                special_prime_count += 1  # count 하기

    print(f"#{tc} {special_prime_count}")
