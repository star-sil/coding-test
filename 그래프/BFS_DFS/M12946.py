# 육각 보드
import sys
sys.setrecursionlimit(1000000)
N = int(input())

graph = [input() for _ in range(N)]
color = [[-1] * N for _ in range(N)]
dx = [-1,-1,0,0,1,1]
dy = [0,1,-1,1,-1,0]

ans = 0

def dfs(x,y,c):
    global ans
    color[x][y] = c
    ans = max(ans,1)
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if graph[nx][ny] == 'X':
                if color[nx][ny] == -1:
                    dfs(nx, ny, c-1)
                ans = max(ans,2)
                if color[nx][ny] == c:
                    ans = max(ans,3)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'X' and color[i][j] == -1:
            dfs(i,j,0)

print(ans)
