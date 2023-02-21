# 2xn 타일링 2 - 5m 47s

n = int(input())

dp = [0] * (1001) # n+1로 하면 n이 1일때 7줄에서 index를 벗어남

dp[1], dp[2] = 1, 3

for i in range(3,n+1):
    dp[i] = dp[i-1] + 2 * dp[i-2]

print(dp[n] % 10007)