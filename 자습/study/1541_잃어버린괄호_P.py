ex = input()

ex_ls = []
sub = ''
for i in range(len(ex)):
    if ex[i] == '-' or ex[i] == '+':
        ex_ls.append(int(sub))
        ex_ls.append(ex[i])
        sub = ''
    else:
        sub += ex[i]

    if i == len(ex) - 1:
        ex_ls.append(int(sub))

answer = ex_ls[0]
sub_ans = 0
i = 1
if len(ex_ls) >= 2:
    while True:
        if ex_ls[i] == '-':
            for j in range(i + 1, len(ex_ls)):
                if ex_ls[j] == '+':
                    pass
                elif ex_ls[j] == '-':
                    answer -= sub_ans
                    sub_ans = 0
                    i = j
                    break
                else:
                    sub_ans += ex_ls[j]
                if j == len(ex_ls) - 1:
                    answer -= sub_ans
                    i = j
        if ex_ls[i] == '+':
            answer += ex_ls[i + 1]
            i += 1
        if i == len(ex_ls) - 1:
            break
        else:
            if ex_ls[i] != '+' and ex_ls[i] != '-':
                i += 1
print(answer)
