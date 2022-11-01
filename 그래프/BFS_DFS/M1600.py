#말이 되고픈 원숭이
import sys
from collections import deque
K = int(input())
W, H = map(int,input().split())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(H)]
dist = [[[-1] * (K+1) for _ in range(W)] for _ in range(H)]

dx1 = [0,0,-1,1]
dy1 = [1,-1,0,0]
dx2 = [2,2,1,1,-2,-2,-1,-1]
dy2 = [1,-1,2,-2,1,-1,2,-2]

dq = deque()
dq.append((0,0,0))
dist[0][0][0] = 0

while dq:
    x,y,p = dq.popleft()

    for i in range(4):
        nx = x + dx1[i]
        ny = y + dy1[i]
        if 0 <= nx < H and 0 <= ny < W and dist[nx][ny][p] == -1 and a[nx][ny] == 0:
            dist[nx][ny][p] = dist[x][y][p] + 1
            dq.append((nx,ny,p))
    
    if p < K:
        p += 1
        for i in range(8):
            nx = x + dx2[i]
            ny = y + dy2[i]
            if 0 <= nx < H and 0 <= ny < W and dist[nx][ny][p] == -1 and a[nx][ny] == 0:
                dist[nx][ny][p] = dist[x][y][p-1] + 1
                dq.append((nx,ny,p))
    
ans = -1
for i in range(K+1):
    if ans == -1:
        ans = dist[H-1][W-1][i]
    else:
        if dist[H-1][W-1][i] != -1:
            ans = min(ans,dist[H-1][W-1][i])
print(ans)