N = int(input())

check_l = []
i = 666
while True:
    if len(check_l) == N:
        break
    if '666' in str(i):
        check_l.append(i)
    i += 1

print(check_l[-1])
