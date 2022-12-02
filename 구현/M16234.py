# 인구 이동
from collections import deque

n,l,r = map(int,input().split())

g = [list(map(int,input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]


a = 0
while True:
    u = [[-1] * n for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(n):
            if u[i][j] == -1:
                dq = deque()
                dq.append((i,j))
                u[i][j] = cnt
                while dq:
                    x, y = dq.popleft()

                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and u[nx][ny] == -1:
                            if l <= abs(g[x][y] - g[nx][ny]) <= r:
                                u[nx][ny] = u[x][y]
                                dq.append((nx,ny))
                cnt += 1

    ans = [[0,0] for _ in range(cnt)]

    for i in range(n):
        for j in range(n):
            ans[u[i][j]][0] += g[i][j]
            ans[u[i][j]][1] += 1
    go = False

    for i in ans:
        if i[1] > 1:
            go = True
    if go:
        for i in range(len(ans)):
            ans[i][0] //= ans[i][1]
        
        for i in range(n):
            for j in range(n):
                g[i][j] = ans[u[i][j]][0]
        a += 1
        continue

    break


print(a)



