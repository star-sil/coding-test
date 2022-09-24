#적록색약
from collections import deque

N = int(input())
dx, dy = [0,0,1,-1], [1,-1,0,0]
graph = [list(input()) for _ in range(N)]
visit = [[False] * N for _ in range(N)]

def bfs(x,y,w):
    dq = deque()
    dq.append((x,y))
    visit[x][y] = True
    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visit[nx][ny] and graph[nx][ny] in w:
                    dq.append((nx,ny))
                    visit[nx][ny] = True


ans1 = 0
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            ans1 += 1
            bfs(i,j,[graph[i][j]])

print(ans1,end=' ')
visit = [[False] * N for _ in range(N)]

ans2 = 0
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            ans2 += 1
            if graph[i][j] == 'R' or graph[i][j] == 'G':
                bfs(i,j,['R','G'])
            else:
                bfs(i,j,[graph[i][j]])

print(ans2)
            


