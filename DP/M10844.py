# 쉬운 계단 수 - 25m38s

dq = [[0] * 10 for _ in range(100)]

for i in range(100):
    for j in range(10):
        if i == 0 and j == 0:
            continue

        if i == 0:
            dq[i][j] = 1
            continue

        if j < 9:
            dq[i][j] = dq[i-1][j+1]
        if j > 0:
            dq[i][j] += dq[i-1][j-1]

        dq[i][j] %= 1000000000

n = int(input())

ans = 0

print(sum(dq[n-1]) % 1000000000)