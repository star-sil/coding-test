# 연속합

n = int(input())
a = list(map(int,input().split()))
dp = [0] * n

for i in range(n):
    dp[i] = a[i]

    if i == 0: continue
    if dp[i-1] + a[i] > a[i]:
        dp[i] = dp[i-1] + a[i]

print(max(dp))
