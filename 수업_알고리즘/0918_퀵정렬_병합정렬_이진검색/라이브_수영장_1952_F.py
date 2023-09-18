import sys

sys.stdin = open("1952_input.txt")

T = int(input())
for tc in range(1, T + 1):
    # p1 = 하루요금
    # p2 = 한달요금
    # p3 = 세달요금
    # p4 = 1년요금
    p1, p2, p3, p4 = map(int, input().split())
    month = list(map(int, input().split()))

    print(p1, p2, p3, p4)
    print(month)

    price = 0

    for i in month:
        if i != 0 and i <= p2 / p1:
            price += (i * p1)
        if i >= p2 / p1:
            price += p2

    print(price)
