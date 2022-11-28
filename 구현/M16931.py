# 겉넓이 구하기 => 맞는거 같은데 틀리다...
# 한번 내려갔을때 넓이를 더해주고 이후에 추가로 올라갈때 더하지 않는다. (세로 첫번째 줄)
'''
3 4
2 3 4
1 2 3
2 2 3
3 2 4
79 -> 정답 80
'''
# 작아졌다 커졌다 하는 로직 확인
n, m = map(int,input().split())

g = [list(map(int,input().split())) for _ in range(m)]

w = 0
# 위 아래 겉넓이 구하기
w += (n * m * 2)

# 옆 겉넓이 구하기
tw = 0
for i in range(m):
    mw = 0
    for j in range(n):
        mw = max(g[i][j],mw)
    tw += mw

for i in range(n):
    mw = 0
    for j in range(m):
        mw = max(g[j][i],mw)
    tw += mw

w += tw * 2

# 볼록 겉넓이 구하기
for i in range(m):
    s = 0
    for j in range(n-1):
        if g[i][j] > g[i][j+1]:
            s += 1
        if g[i][j] < g[i][j+1]:
            if s > 0:
                w += s + (g[i][j+1] - g[i][j])
                s = 0

for i in range(n):
    s = 0
    for j in range(m-1):
        if g[j][i] > g[j+1][i]:
            s += 1
        if g[j][i] < g[j+1][i]:
            if s > 0:
                w += s + (g[j+1][i] - g[j][i])
                s = 0

print(w)
            



