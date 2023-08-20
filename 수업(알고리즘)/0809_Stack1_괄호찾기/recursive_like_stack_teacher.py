def funfun(n):
    # 1. 종료 조건
    if n == 0:
        print(f"{n} : 끝")
        return

    # 2. 재귀 호출(언제)
    else:
        print(n)
        funfun(n - 1)
        print(n)


funfun(10)
