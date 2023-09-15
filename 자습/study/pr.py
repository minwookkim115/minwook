S = input()

al_l = []
for i in range(97, 123):
    al_l.append(chr(i))
print(al_l)

answer_l = [-1] * 26

print(answer_l)

for i in range(len(S)):
    print(S[i])
    for j in range(len(al_l)):
        if S[i] == al_l[j]:
            if answer_l[j] == -1:
                answer_l[j] = i
                break

print(*answer_l)