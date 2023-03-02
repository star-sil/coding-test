# 정수 삼각형
# j의 범위를 잘못 설정했다. 제출 코드 확인

n = int(input())

dp = [[0]]

for i in range(1,n+1):
    a = list(map(int,input().split()))
    tmp = []

    if i == 1:
        dp.append([a[0]])
        continue

    for j in range(len(a)):
        if j == 0:
            tmp.append(dp[i-1][0] + a[j])
            continue
        if j == i-1:
            tmp.append(dp[i-1][-1] + a[j])
            continue
        tmp.append(max(dp[i-1][j-1], dp[i-1][j])+a[j])

    dp.append(tmp)

print(max(dp[n]))
