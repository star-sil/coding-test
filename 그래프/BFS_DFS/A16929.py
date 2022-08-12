#Two Dots
import sys
sys.setrecursionlimit(10**7)
N, M = map(int,input().split())

graph = []
visited = [[False] * M for _ in range(N)]
dx = [0,1,-1,0]
dy = [1,0,0,-1]

def dfs(x,y,px,py,color):
    if(visited[x][y]): 
        return True
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if not (nx == px and ny == py) and color == graph[nx][ny]:
                if(dfs(nx,ny,x,y,color)): 
                    return True
    return False

for _ in range(N):
    graph.append(sys.stdin.readline().strip())

for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        color = graph[i][j]
        if(dfs(i,j,i,j,color)):
            print('YES')
            exit()
print('NO')




