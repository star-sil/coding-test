#데스 나이트
from collections import deque
N = int(input())
dist = [[-1] * N for _ in range(N)]
dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

start_x, start_y, end_x, end_y = map(int,input().split())
dq = deque()
dq.append((start_x,start_y))
dist[start_x][start_y] = 0

while dq:
    x, y = dq.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < N and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            dq.append((nx,ny))

print(dist[end_x][end_y])