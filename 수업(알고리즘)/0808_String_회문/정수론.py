# 최대 공약수 GCD : GREATEST COMMON DIVISOR
# 최소 공배수 LCM : LEAST COMMON MULTIPLE

# 최대 공약수
# a > b
# 더 작은 수(b) 부터 1씩 감소하는 값으로
# 더 큰수(a)를 나눌 때 나머지가 0 & 자기자신(b)을 나눌 때 나머지가 0
def gcd(a, b):
    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


# 유클리드 호제법
# a > b
# a, b 의 최대 공약수
# a 와 b, a를 b로 나눈 나머지 r 이 있다고 했을 때 다음이 성립한다.
# a, b의 최대 공약수는 b와 r의 최대 공약수와 같다
# 재귀적으로 (a, b) == (b, r)
# new_gcd(a, b) == new_gcd(b, r)
# b가 0인 경우는 생각하지 않음 => 어떤 미친놈이 4 와 0 의 최대 공약수를 구하겠나

def new_gcd(a, b):
    # 종료 조건
    if b == 0:
        return a
    # 재귀 호출
    else:
        return new_gcd(b, a % b)


# 최소 공배수
# a와 b의 최소 공배수는
# a와 b의 곱을 a와 b의 최대 공약수로 나눈것과 같다.
def lcm(a, b):
    return a * b // new_gcd(a, b)


a = 20
b = 15
print(gcd(a, b))
print(lcm(a, b))
print(new_gcd(a, b))
