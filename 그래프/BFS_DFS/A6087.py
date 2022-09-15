#레이저 통신
#가중치를 파악하지 못해 문제를 잘못 접근했다.
# 0-1 BFS로 구현하면 되지만 방문한 점을 추가로 비교해야된다는 번거로움이 있다. 
from collections import deque

W, H = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,1,-1]
graph = []
target = []
MAX = 10001
for i in range(H):
    tmp = list(input())
    for j in range(len(tmp)):
        if tmp[j] == 'C':
            target.append((i,j))
    graph.append(tmp)

dist = [[MAX] * W for _ in range(H)]

dq = deque()
dq.append((target[0][0],target[0][1],-1,0))
dist[target[0][0]][target[0][1]] = 0

while dq:
    x,y,d,mirror = dq.popleft()
    if mirror > dist[x][y]:
        continue

    dist[x][y] = mirror

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < H and 0 <= ny < W:
            if graph[nx][ny] != '*':
                mirror = dist[x][y]
                if d == i or d == -1:
                    dq.appendleft((nx,ny,i,mirror))
                else:
                    mirror += 1
                    dq.append((nx,ny,i,mirror))

print(dist[target[1][0]][target[1][1]])