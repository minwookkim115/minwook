import sys

N = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().strip()))
M = int(sys.stdin.readline().strip())
check_num = list(map(int, sys.stdin.readline().strip()))


for i in range(M):
    if check_num[i] in num:
        check_num[i] = 1
    else:
        check_num[i] = 0

print(*check_num)