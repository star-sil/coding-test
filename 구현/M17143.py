# 낚시왕

r,c,m = map(int,input().split()) # 행, 열, 상어수

g = [[(0,0,0)] * c for _ in range(r)]
sharks = []

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def shift(new_g,sr,sc):
    s,d,z = g[sr][sc]

    for _ in range(s):
        sr, sc = sr + dx[d], sc + dy[d]

        if sr < 0 or sr >= r or sc < 0 or sc >= c:
            if d == 0 or d == 1:
                d = 1 - d
            elif d == 2 or d == 3:
                d = 5 - d
            
            sr, sc = sr + 2 * dx[d], sc + 2 * dy[d]
    
    if new_g[sr][sc][2] > 0:
        if new_g[sr][sc][2] > z:
            return
    
    new_g[sr][sc] = (s,d,z)

        

for _ in range(m):
    sr,sc,s,d,z = map(int,input().split())
    g[sr-1][sc-1] = (s,d-1,z)

ans = 0
for i in range(c):
    for j in range(r):
        if g[j][i][2] > 0:
            ans += g[j][i][2]
            g[j][i] = (0,0,0)
            break
    
    new_g = [[(0,0,0)] * c for _ in range(r)]

    for j in range(r):
        for k in range(c):
            if g[j][k][2] > 0:
                shift(new_g,j,k)

    g = new_g

print(ans)