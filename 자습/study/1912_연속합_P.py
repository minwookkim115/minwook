# N = int(input())
# numbers = list(map(int, input().split()))
#
# answer = -10000
# a = 1
# b = 0
#
# while True:
#     sub = 0
#     for i in range(b, a):
#         sub += numbers[i]
#     answer = max(answer, sub)
#
#     a += 1
#
#     if a == N + 1:
#         b += 1
#         a = b + 1
#
#     if b == N:
#         break
#
# print(answer)

N = int(input())
numbers = list(map(int, input().split()))

for i in range(1, N):
    numbers[i] = max(numbers[i], numbers[i] + numbers[i - 1])

print(max(numbers))