# 로봇 청소기

n, m = map(int,input().split())
x,y,d = map(int,input().split())

g = [list(map(int,input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]


dd = [3,0,1,2]
dx = [0,-1,0,1]
dy = [-1,0,1,0]
visit[x][y] = True
go = True
ans = 1

while go:
    isClean = False

    # 4방향 중 청소를 할 수 있는 방향이 있는지 확인
    for _ in range(4):
        nx , ny = x + dx[d], y + dy[d]
        d = dd[d]
        
        if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0:
            if not visit[nx][ny]:
                visit[nx][ny] = True
                x,y = nx, ny
                ans += 1
                isClean = True
                break
    
    if isClean:
        continue
    
    # 4방향 모두 청소가 되어있거나 벽이 있는 경우 바라보는 기준 후진할 수 있는지 확인
    nx, ny = x + dx[dd[d]], y + dy[dd[d]]
    if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0:
        x, y = nx, ny
    else:
        go = False

print(ans)
    





