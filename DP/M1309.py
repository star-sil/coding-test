# 동물원 - 10m 33s

dp = [[0,0,0] for _ in range(100001)]
dp[0][0] = 1
mod = 9901

n = int(input())

for i in range(1,n+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % mod
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % mod
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % mod

print(sum(dp[n]) % mod)