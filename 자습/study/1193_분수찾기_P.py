N = int(input())

i = 1
j = 2

check = []

while True:
    if i >= 20000000:
        break
    check.append(i)
    i += j
    j += 1

# print(check)
num = 1
for i in range(len(check)):
    if N <= check[i]:
        num += i
        break

pos = N - check[num-2]

ans1 = 0
ans2 = 0
if num % 2 == 0:
    ans1 = 1
    ans2 = num
else:
    ans1 = num
    ans2 = 1

if pos >= 2:
    for _ in range(2, pos + 1):
        if num % 2 == 0:
            ans1 += 1
            ans2 -= 1
        else:
            ans1 -= 1
            ans2 += 1

print(f"{ans1}/{ans2}")