import sys
sys.stdin = open("16904_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    time = []
    for i in range(0, N):
        s, e = map(int, input().split())
        time.append([s, e])
    print(time)
    # time.sort(key= lambda x:x[0])
    time.sort(key=lambda x: x[1])
    print(time)

    cnt = 1
    j = 0
    for i in range(N):
        if time[i][0] >= time[j][1]:
            cnt += 1
            j = i

    print(f"#{tc} {cnt}")
