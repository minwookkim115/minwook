N = int(input())
str_l = [input() for _ in range(N)]
str_l = list(set(str_l))

answer_l = []
check = 0
for i in range(len(str_l)):
    for j in range(len(str_l)):
        if len(str_l[i]) <= len(str_l[j]):
            if str_l[i] == str_l[j][:len(str_l[i])]:
                check += 1
    if check == 1:
        answer_l.append(str_l[i])
        check = 0
    else:
        check = 0

print(len(answer_l))
