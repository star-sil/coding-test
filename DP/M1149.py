# RGB거리 - 48m 16s
# 문제를 잘못 이해해서 시간 오래걸림....테케 보면서 이해한 내용이 맞는지 확인하자..
# 모든 이웃이 같으면 안된다는 것 중요!! -> 모든 이웃이 다 달라야한다는 것으로 이해했다.


house = []
n = int(input())
dp = [[0,0,0] for _ in range(n)]

for i in range(n):
    house.append(list(map(int,input().split())))

for i in range(n):
    if i == 0:
        dp[i][0] = house[i][0]
        dp[i][1] = house[i][1]
        dp[i][2] = house[i][2]
        continue

    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + house[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + house[i][1]
    dp[i][2] = min(dp[i-1][1],dp[i-1][0]) + house[i][2]

print(min(dp[n-1]))


