# 포도주 시식

dp = [[0,0,0] for _ in range(10001)]

n = int(input())

a = [int(input()) for i in range(n)]

for i in range(1,n+1):

    dp[i][0] = max(dp[i-1][0],dp[i-1][1],dp[i-1][2])
    dp[i][1] = dp[i-1][0] + a[i-1]
    dp[i][2] = dp[i-1][1] + a[i-1]

print(max(dp[n]))