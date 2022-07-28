#미로 탐색

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
g = [[] for i in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
dq = deque()

for i in range(N):
    str = sys.stdin.readline()
    for j in str:
        if j == "1":
            g[i].append(1)
        elif j == "0":
            g[i].append(0)

def bfs():
    while len(dq) > 0:
        x, y, z = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            print(x,y,nx,ny,z)
            if nx >= 0 and ny >= 0 and nx < N and ny < M:
                if g[nx][ny] == 1:
                    g[nx][ny] = (z + 1)
                    dq.append((nx,ny,(z+1)))
        
dq.append((0,0,1))
g[0][0] = 0
bfs()
print(g[N-1][M-1])