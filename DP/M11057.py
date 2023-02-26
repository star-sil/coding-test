# 오르막 수 - 8m 52s

dp = [[0] * 10 for _ in range(1001)]
mod = 10007

n = int(input())

for i in range(10):
    dp[1][i] = 1


for i in range(2,n+1):
    for j in range(10):
        for k in range(j,10):
            dp[i][j] += dp[i-1][k]
        dp[i][j] %= mod

print(sum(dp[n]) % mod)
