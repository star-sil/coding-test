#미세먼지 안녕!

# 배열 회전 로직 숙지
# 미세먼지가 확산할때 모든 곳의 미세먼지가 같이 확산해야한다.
# 미세먼지가 확산할때 또다른 미세먼지(a)로 환산이 되면 추후에 a가 확산할때
# 본래 미세먼지와 다른 미세먼지를 확산시키므로 배열을 새로 생성해 받아야 한다.

dx = [0,-1,0,1]
dy = [1,0,-1,0]
n, m, t = map(int,input().split())

# 미세먼지
a = [list(map(int,input().split())) for _ in range(n)]
# 확산된 미세먼지를 저장하기 위한 그래프
b = [[0]*m for _ in range(n)]

x = 0
y = 0

# 공기청정기 위치 찾기
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            x = i
            y = j
x -= 1

# 공기청정기 작동 구현 (시계방향 반시계방향 동시 구현함)
def go(sx, sy, z):
    # 이전 칸의 미세먼지 값
    prev = 0
    x = sx
    y = sy+1 # 공기청정기 오른쪽 한칸부터 미세먼지 이동 시작
    k = 0
    while True:
        if x == sx and y == sy:
            break

        # 값 옮기기
        temp = prev
        prev = a[x][y]
        a[x][y] = temp

        # 기존 방향으로 움직이기
        x += dx[k]
        y += dy[k]

        # 기존 방향으로 움직이지 못하는 경우
        if x < 0 or y < 0 or x >= n or y >= m:

            # 다시 뒤로 이동
            x -= dx[k]
            y -= dy[k]

            # 방향 변경하기 z는 다음 방향을 결정하기 위한 값
            k += z
            k %= 4
            x += dx[k]
            y += dy[k]


for _ in range(t):
    for i in range(n):
        for j in range(m):
            # 공기청정기면 넘어가기
            if a[i][j] <= 0:
                continue

            cnt = 0
            for k in range(4): # 미세먼지 확산 가능한 뱡향 갯수 파악하기
                nx = i+dx[k]
                ny = j+dy[k]
                if 0 <= nx < n and 0 <= ny < m and a[nx][ny] >= 0:
                    cnt += 1

            if cnt > 0: # 확산가능한 방향이 존재하면 확산 동시에 일어나야하므로 별도의 그래프에 저장
                val = a[i][j] // 5
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0 <= nx < n and 0 <= ny < m and a[nx][ny] >= 0:
                        b[nx][ny] += val
                a[i][j] = a[i][j] - cnt * val
    
    # 확산 결과 옮기기
    for i in range(n):
        for j in range(m):
            if a[i][j] == -1:
                continue
            a[i][j] += b[i][j]
            b[i][j] = 0
    go(x,y,1)
    go(x+1,y,3)

ans = 0

for i in range(n):
    for j in range(m):
        if a[i][j] >= 0:
            ans += a[i][j]
print(ans)







