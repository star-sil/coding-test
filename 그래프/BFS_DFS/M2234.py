#성곽
#방문 여부를 계속 체크하는 부분에서 시간이 뺏겨 시간 초과가 날 확률이 높다.
#따라서 방문 여부를 체크하는 방식을 같은 방에 속하는지의 여부로 하면
#방문 여부를 체크하는 동시에 같은 방인지까지 알 수 있다.
#비트 연산도 알아두면 좋을 듯 하다.
from collections import deque

n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(m)]
wall = [8,4,2,1] # 남 -> 동 -> 북 -> 서
dx, dy = [1,0,-1,0], [0,1,0,-1] # x가 세로 y가 가로 방향: 남 -> 동 -> 북 -> 서
visit = [[0] * n for _ in range(m)]


def bfs(sx,sy,rooms):
    dq = deque()
    dq.append((sx,sy))
    visit[sx][sy] = rooms
    count = 0
    while dq:
        x, y = dq.popleft()
        w = a[x][y]
        count += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 이전 정점을 방문을 한경우도 이전 정점에 대한 방향에 벽이 존재하는지 정검하기 위해
            # 방문여부를 체크하기 전에 벽이 있는지 확인해야한다.
            if (w - wall[i]) >= 0:
                w -= wall[i]
                continue
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == 0:
                visit[nx][ny] = rooms
                dq.append((nx,ny))
    return count

ans1 = 0 #전체 방의 개수
ans2 = 0 #가장 큰 방의 크기
room = [0]
for i in range(m):
    for j in range(n):
        if visit[i][j] == 0:
            ans1 += 1
            room.append((bfs(i,j,ans1)))
print(ans1)

for i in range(1,ans1+1):
    ans2 = max(ans2,room[i])
print(ans2)

ans3 = 0
for i in range(m):
    for j in range(n):
        w = a[i][j]
        for k in range(4):
            if w - wall[k] >= 0:
                w -= wall[k]
                ni, nj = i + dx[k], j + dy[k]
                if 0 <= ni < m and 0 <= nj < n:
                    #벽을 없애고 이동한 방과 같은 방 인경우 같은 그룹이므로 더해주면 안된다.
                    if visit[i][j] == visit[ni][nj]:
                        continue
                    ans3 = max(ans3,room[visit[i][j]] + room[visit[ni][nj]])

print(ans3)