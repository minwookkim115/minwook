N = int(input())
money = list(map(int, input().split()))
grade = input()

answer = 0
last_month = 0
check = 0
for i in range(N):
    if grade[i] == 'B':
        check = money[0] - 1
        last_month = abs(last_month - check)
        answer += last_month
    if grade[i] == 'S':
        check = money[1] - 1
        last_month = abs(last_month - check)
        answer += last_month
    if grade[i] == 'G':
        check = money[2] - 1
        last_month = abs(last_month - check)
        answer += last_month
    if grade[i] == 'P':
        check = money[3] - 1
        last_month = abs(last_month - check)
        answer += last_month
    if grade[i] == 'D':
        check = money[3]
        answer += check

print(answer)