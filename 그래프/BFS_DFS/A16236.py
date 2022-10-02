#아기 상어
#방문 순서와 관련이 없다.
#방문 순서를 정해준 이유는 bfs로 최단 거리 탐색을 하는경우 거리가 겹치는 경우가 생기는데 이때 어떤 것을 먼저
#방문 해야 하는지를 알려주기 위함이다. 방문순서는 상관이 없다.
from collections import deque

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
dx = [-1,0,0,1]
dy = [0,-1,1,0]

def bfs(graph,x,y,s):
    dq = deque()
    dq.append((x,y))
    dist = [[-1] * N for _ in range(N)]
    dist[x][y] = 0
    fish = []
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
                size = False
                go = False
                if graph[nx][ny] == 0 or graph[nx][ny] == s:
                    go = True
                elif graph[nx][ny] < s:
                    go = True
                    size = True
                
                if go:
                    dq.append((nx,ny))
                    dist[nx][ny] = dist[x][y] + 1
                    if size:
                        fish.append((dist[nx][ny],nx,ny))
    
    if not fish:
        return None
    fish.sort()
    return fish[0]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark = [i,j]
            graph[i][j] = 0

ans = 0
shark_size = 2
exp = 0

while True:
    p = bfs(graph,shark[0],shark[1],shark_size)
    if p is None:
        break
    dist, nx, ny = p
    graph[nx][ny] = 0
    ans += dist
    exp += 1
    if shark_size == exp:
        shark_size += 1
        exp = 0
    shark[0], shark[1] = nx, ny

print(ans)