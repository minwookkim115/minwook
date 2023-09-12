import keyword
string = "바나나"

number = 10

print(type(string))  # srting 이라는 변수의 타입이 궁금하다.
print(type(number))  # number 라는 변수의 타입이 궁금하다.


# 변수
# 할당 연산자 = 를 통해서 할당해야 한다.
# 변수 x 안에 "ssafy"라는 문자열을 저장한다.
x = "ssafy"

# "ssafy" 라는 문자열을 세번 출력하고 싶다.

print("ssafy")
print("ssafy")
print("ssafy")

print(x)
print(x)
print(x)

result = 3 + 5
print(result)

# 변수이름으로 쓰면 안되는 것들 리스트

print(keyword.kwlist)

# print = "이런식으로 문자열을 할당하면"
# print(5) => 오류가 나옴 / print 가 더이상 함수의 역할을 할 수 없다.

# +, * 연산자는 문자에도 가능
str1 = "안녕하세요"
str2 = "반갑습니다"

str3 = str1 + str2
print(str3)
print(str3 * 2)

# height 가 직관적으로 변수를 이해하기 쉬움
a = 180
height = 180

# 파이썬에서는 한글로도 변수가능 (근데 잘 안씀)
파이썬 = 170

# Alt + Shift + f => 정렬해줌
