def itoa(a):
    s = ''
    while a > 0:
        s += chr(ord("0") + a % 10)  # (1의자리 숫자의 ASCII 값)
        a //= 10

    return s[::-1]


a = 123
print(itoa(a))
