import sys

sys.stdin = open("1859_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):

    N = int(input())
    price_d = list(map(int, input().split()))

    print(price_d)

    ex_val = price_d[N - 1]
    sold_price = 0

    for i in range(N - 2, -1, -1):
        if ex_val > price_d[i]:
            sold_price += ex_val - price_d[i]

        if ex_val < price_d[i]:
            ex_val = price_d[i]

    print(f"#{tc} {sold_price}")
