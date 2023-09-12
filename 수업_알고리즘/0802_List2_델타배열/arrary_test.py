'''
3
1 2 3
4 5 6
7 8 9
'''

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

total1 = 0
total2 = 0

for i in range(N):
    total1 += arr[i][i]  # (0,0) (1,1) (2,2)
    total2 += arr[i][N - 1 - i]  # (0,2) (1,1) (2,0)

print(total1, total2)
