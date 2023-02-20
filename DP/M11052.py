# 카드 구매하기 - 35m 45s

n = int(input())
cards = [0] + list(map(int,input().split()))

dp = [0] * 1001

for i in range(1,n+1):
    dp[i] = cards[i]
    for j in range(1,i//2+1):
        dp[i] = max(dp[i],dp[j] + dp[i-j])

print(dp[n])