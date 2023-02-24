# 합분해 - x
# 틀린 로직


n, m = map(int,input().split())
dq = [[0] * 201 for _ in range(201)]

for i in range(201):
    dq[0][i] = 1

for i in range(1,201):
    for j in range(201):
        for k in range(1,i+1):
            dq[i][j] += dq[i-k][j-1] # j개의 정수로 i 만들
        dq[i][j] %= 1000000000

print(dq[n][m] % 1000000000)