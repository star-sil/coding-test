#아기 상어 2
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
dx, dy = [0,0,1,-1,1,-1,1,-1], [1,-1,0,0,1,-1,-1,1]
shark_pos = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            shark_pos.append((i,j))

def bfs(x,y,sharks):
    dist = [[-1] * M for _ in range(N)]
    dq = deque()
    dq.append((x,y))
    dist[x][y] = 0
    while dq:
        x,y = dq.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                dq.append((nx,ny))
    long = -1
    for i,j in sharks:
        if long == -1:
            long = dist[i][j]
        long = min(dist[i][j],long)
    return long

ans = -1
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            continue
        distance = bfs(i,j,shark_pos)
        if ans == -1:
            ans = distance
        else:
            ans = max(ans,distance)

print(ans)