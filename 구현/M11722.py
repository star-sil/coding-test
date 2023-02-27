# 가장 긴 감소하는 부분 수열 - 11m 54s
n = int(input())

a = list(map(int,input().split()))
dp = [0] * n
dp[0] = 1

for i in range(1,n):
    dp[i] = 1

    for j in range(i):
        if a[j] > a[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
print(max(dp))