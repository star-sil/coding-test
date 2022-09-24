#연구소
#벽을 세우고 탐색을 한다.벽을 세우는 모든 경우의 수와 탐색의 시간의 복잡도가 작아 시간초과가 안난다.

from collections import deque
N, M = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
li = []

dq = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            dq.append((i,j))
            li.append((i,j))


def bfs():
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                dq.append((nx,ny))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
            elif graph[i][j] == 2:
                graph[i][j] = 0
    for i, j in li:
        graph[i][j] = 2
        dq.append((i,j))
    return cnt

ans = 0
for x1 in range(N):
    for y1 in range(M):
        if graph[x1][y1] != 0: continue
        graph[x1][y1] = 1
        for x2 in range(N):
            for y2 in range(M):
                if graph[x2][y2] != 0: continue
                graph[x2][y2] = 1
                for x3 in range(N):
                    for y3 in range(M):
                        if graph[x3][y3] != 0: continue
                        graph[x3][y3] = 1
                        ans = max(bfs(),ans)
                        graph[x3][y3] = 0
                graph[x2][y2] = 0
        graph[x1][y1] = 0


print(ans)
