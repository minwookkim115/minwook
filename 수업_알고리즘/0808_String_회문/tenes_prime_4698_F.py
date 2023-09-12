import sys

sys.stdin = open("4698_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    D, A, B = map(int, input().split())

    is_prime = [True for _ in range(B + 1)]  # 모두 소수라고 가정

    # 0 ~ B + 1 까지의 소수가 아닌 것은 False 로 변경
    for i in range(2, int(B**0.5) + 1):
        if is_prime[i]:
            j = 2
            while i * j <= B:
                is_prime[i * j] = False
                j += 1

    # A부터 B까지 소수인 수를 문자열 리스트로 받는 리스트 생성
    prime = []
    for i in range(A, B + 1):
        if is_prime[i] is True:
            prime.append(list(str(i)))

    # 1은 소수가 아니므로 제외
    prime.remove(prime[0])

    print(prime)

    # prime 에서 D가 포함된 리스트 개수 세기
    special_prime_count = 0
    for i in prime:
        for j in i:
            if j == str(D):
                special_prime_count += 1
                break

    print(f"#{tc} {special_prime_count}")
