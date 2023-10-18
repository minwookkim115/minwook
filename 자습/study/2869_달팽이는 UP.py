A, B, V = map(int,input().split())

a = A - B
b = V - A

answer = 1
if b % a > 0:
    answer += 1
    answer += b // a
else:
    answer += b // a

print(answer)