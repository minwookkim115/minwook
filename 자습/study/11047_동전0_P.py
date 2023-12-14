N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]

answer = 0
while K > 0:
    for i in range(N - 1, -1, -1):
        check = K // coin[i]
        if check >= 1:
            answer += check
            K -= check * coin[i]

print(answer)
