N = int(input())

sub, answer = 1, 0

for i in range(N + 1):
    sub, answer = answer, answer + sub

print(answer % 10007)
