# 제곱수의 합 - 44m34s
# 백트래킹을 적용해도 메모리, 시간 초과 발생...
# 해당 방식은 O(n^2)으로 시간 초과가 발생한다.
# 테케는 통과했지만 옳바른 방식이 아님

import math

n = int(input())
sq = int(math.sqrt(n))
dp = [-1] * (100000)

dp[1] = 1
dp[2] = 2

for i in range(3,n+1):

    for j in range(2,sq+1):
        if j*j == i:
            dp[i] = 1

    for j in range(1,i//2+1):
        if dp[i] == -1 or dp[j] + dp[i-j] < dp[i]:
            dp[i] = dp[j] + dp[i-j]

print(dp[n])






