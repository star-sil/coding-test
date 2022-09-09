#벽 부수고 이동하기
# 방문 그래프는 3차배열이 되어야한다. 왜냐하면 같은 노드일지라도 벽을 부수고
# 이동하는 경우와 벽을 부수지 않고 이동하는 경우 다른 노드로 취급되어야 된다.
# 만약 두 노드를 구분하지 않으면 벽을 부수고 이동하는 경로와 벽을 부수지 않고 이동하는 경로가 겹친다.
import sys
from collections import deque
N, M = map(int, input().split())
graph = []
dist = [[[-1] * 2 for i in range(M)] for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
for _ in range(N):
    line = sys.stdin.readline()
    tmp = []
    for i in range(M):
        if line[i] == '0':
            tmp.append(0)
        else:
            tmp.append(1)
    graph.append(tmp)
dq = deque()
dq.append((0,0,0))
dist[0][0][0] = 1

while dq:
    x, y, p = dq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx  < N and ny >= 0 and ny < M:
            if graph[nx][ny] == 0 and dist[nx][ny][p] == -1:
                dist[nx][ny][p] = dist[x][y][p] + 1
                dq.append((nx,ny,p))
            if p == 0 and graph[nx][ny] == 1 and dist[nx][ny][p+1] == -1:
                dist[nx][ny][p+1] = dist[x][y][p] + 1
                dq.append((nx,ny,p+1))


if dist[N-1][M-1][0] != -1 and dist[N-1][M-1][1]  != -1:
    print(min(dist[N-1][M-1]))
elif dist[N-1][M-1][0] != -1:
    print(dist[N-1][M-1][0])
elif dist[N-1][M-1][1] != -1:
    print(dist[N-1][M-1][1])
else:
    print(-1)
                

        
