student_l = []
for i in range(28):
    student = int(input())
    student_l.append(student)

check = [0] * 31
for i in range(28):
    check[student_l[i]] = 1

no_student = []
for i in range(30):
    if check[i] == 0:
        no_student.append(i)

no_student.pop(0)
no_min = min(no_student)
no_max = max(no_student)

print(no_min)
print(no_max)