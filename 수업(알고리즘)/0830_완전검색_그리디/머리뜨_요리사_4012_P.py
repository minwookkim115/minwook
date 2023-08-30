import sys

sys.stdin = open("4012_input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]

    min_v = 20000

    food = []
    for i in range(1, N + 1):
        food.append(i)

    # 부분집합 생성
    for i in range(1, 1 << (N-1)):
        food_a = []
        food_b = []
        for j in range(N):
            if i & (1 << j):
                food_a.append(food[j])
            else:
                food_b.append(food[j])

        # food_a랑 food_b가 정확히 나눠 졌을때
        if len(food_a) == len(food_b) == N//2:
            a = 0
            b = 0
            for o in range(N // 2):
                for p in range(N // 2):
                    if o != p:
                        # a와 b에 각각 더하고
                        a += synergy[food_a[o] - 1][food_a[p] - 1]
                        b += synergy[food_b[o] - 1][food_b[p] - 1]
            # 빼기 절대값
            c = abs(a-b)
            # 최소값
            min_v = min(min_v, c)

    print(f"#{tc} {min_v}")