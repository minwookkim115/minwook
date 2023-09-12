# 개빠르당
def fibo(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# 필요한만큼 저장해두고 불러오자 => DP
dp = [0] * (100 + 1)
dp[0] = 0
dp[1] = 1
for i in range(2, 101):
    dp[i] = dp[i - 1] + dp[i - 2]

print(fibo(100))
