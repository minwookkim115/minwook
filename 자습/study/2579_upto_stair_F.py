N = int(input())

stair_l = [int(input()) for _ in range(N)]


def dp(n):
    DP = [0] * n
    DP[0] = stair_l[0]

    i = 0
    while i < n + 2:
        if i != n - 2:
            if stair_l[i] + stair_l[i + 1] > stair_l[i] + stair_l[i + 2]:
                DP[i + 1] = stair_l[i + 1]
                i += 1
            if stair_l[i] + stair_l[i + 1] < stair_l[i] + stair_l[i + 2]:
                DP[i + 2] = stair_l[i + 2]
                i += 2
            # else:
            #     if stair_l[i + 3] < stair_l[i + 4]:
            #         DP[i + 2] = stair_l[i + 1]
            #     else:
        else:
            DP[n] = stair_l[n]
    return DP


print(dp(N))
