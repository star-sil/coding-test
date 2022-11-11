#벽 부수고 이동하기2
from collections import deque
import sys

N,M,K = map(int,sys.stdin.readline().split())
graph = [list(map(int,list(input()))) for _ in range(N)]
dist = [[[-1] * (K+1) for _ in range(M)] for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
dq = deque()

dq.append((0,0,0))
dist[0][0][0] = 1
while dq:
    x, y, z = dq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if z < K and graph[nx][ny] == 1 and dist[nx][ny][z+1] == -1:
                dist[nx][ny][z+1] = dist[x][y][z] + 1
                dq.append((nx,ny,z+1))
            if graph[nx][ny] == 0 and dist[nx][ny][z] == -1:
                dist[nx][ny][z] = dist[x][y][z] + 1
                dq.append((nx,ny,z))

ans = -1
for i in range(K+1):
    if ans == -1:
        ans = dist[N-1][M-1][i]
    else:
        if dist[N-1][M-1][i] != -1:
            ans = min(ans,dist[N-1][M-1][i])

print(ans)
