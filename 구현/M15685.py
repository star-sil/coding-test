# 드래곤 커브

from collections import deque

g = [[False] * 101 for _ in range(101)]

n = int(input())
dc = [list(map(int,input().split())) for _ in range(n)]

dd = [1,2,3,0]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

for x,y,d,tg in dc:
    g[y][x] = True
    g[y+dy[d]][x+dx[d]] = True
    ng = 0
    dq = deque()
    dq.append(d)
    while ng < tg:
        nds = deque()
        tx, ty = x, y
        for d in dq:
            nds.append(d)
        
        while dq:
            d = dq.pop()
            nd = dd[d]
            nds.append(nd)

        for d in nds:
            nx, ny = tx + dx[d], ty + dy[d]
            g[ny][nx] = True
            tx, ty = nx, ny

        dq = nds
        ng += 1

ans = 0
xk = [0,1,0,1]
yk = [0,0,1,1]
for i in range(100):
    for j in range(100):
        isDragon = True
        for k in range(4):
            nx, ny = i + xk[k], j + yk[k]

            if not g[ny][nx]:
                isDragon = False
        if isDragon:
            ans += 1

print(ans)
        
        




