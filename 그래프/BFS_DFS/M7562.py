import sys
from collections import deque

T = int(input())
dx = [2, 2, -2, -2,-1,1,-1,1]
dy = [-1,1,-1,1,2, 2, -2, -2]

for i in range(T):
    N = int(input())
    g = [[0] * N for i in range(N)]
    x, y = map(int, input().split())
    destX,destY = map(int, input().split())
    dq = deque()
    g[x][y] = 1
    dq.append((x,y,1))
    while len(dq) > 0:
        x,y,cost = dq.popleft()
        cost += 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < N and ny < N:
                if g[nx][ny] == 0:
                    g[nx][ny] = cost
                    dq.append((nx,ny,cost))
    print(g[destX][destY]-1)
