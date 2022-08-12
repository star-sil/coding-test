#알고스팟
from pickle import FALSE
import sys
from collections import deque
M, N = map(int, input().split())

graph = []
visited = [[False] * M for _ in range(N)]
dq = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(N):
    tmp = []
    for j in sys.stdin.readline().strip():
        tmp.append([int(j),0])
    graph.append(tmp)

dq.append([0,0])

while dq:
    x, y = dq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if graph[nx][ny][0] == 0 and visited[nx][ny] == False:
                visited[nx][ny] = True
                dq.appendleft((nx,ny))
                graph[nx][ny][1] = graph[x][y][1]
            if graph[nx][ny][0] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                graph[nx][ny][0] = 0
                graph[nx][ny][1] = graph[x][y][1] + 1
                dq.append((nx,ny))

print(graph[N-1][M-1][1])

    