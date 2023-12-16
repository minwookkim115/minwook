# def fibonacci(n):
#     global one, zero
#     if n == 0:
#         zero += 1
#         return 0
#     elif n == 1:
#         one += 1
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#
#     one = 0
#     zero = 0
#     fibonacci(N)
#
#     print(zero, one)

T = int(input())

for _ in range(T):
    N = int(input())
    zero, one = 1, 0

    for i in range(N):
        zero, one = one, zero + one

    print(zero, one)