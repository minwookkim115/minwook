N = int(input())

answer = 0
for i in range(N):
    a = N - i
    check = 0
    for j in range(len(str(a))):
        check += int(str(a)[j])
    if check == i:
        answer = a

print(answer)