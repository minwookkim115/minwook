N = int(input())
dot = [list(map(int, input().split())) for _ in range(N)]

dot.sort()
for i in dot:
    print(*i)



