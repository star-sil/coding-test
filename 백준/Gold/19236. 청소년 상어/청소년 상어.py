# 청소년 상어

from copy import deepcopy

n = 4
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def go(num, direction, x, y, d):
    for who in range(1, n*n+1): # 물고기 번호 순서대로 찾기
        f = False
        for i in range(n):
            for j in range(n):
                if num[i][j] == who: # 순서인 물고기 번호 찾음
                    for k in range(8): # 알맞은 방향 찾기
                        nx = i+dx[direction[i][j]]
                        ny = j+dy[direction[i][j]]
                        # 알맞은 방향 찾기
                        if 0 <= nx < n and 0 <= ny < n and num[nx][ny] >= 0 and (not (nx == x and ny == y)):
                            num[i][j], num[nx][ny] = num[nx][ny], num[i][j]
                            direction[i][j], direction[nx][ny] = direction[nx][ny], direction[i][j]
                            f = True
                            break
                        else:
                            direction[i][j] += 1
                            direction[i][j] %= 8
                if f:
                    break
            if f:
                break
    answer = 0
    sx = x+dx[d]
    sy = y+dy[d]
    while 0 <= sx < n and 0 <= sy < n:
        if num[sx][sy] != 0:
            temp = num[sx][sy]
            num[sx][sy] = 0
            cur = temp + go(deepcopy(num), deepcopy(direction), sx, sy, direction[sx][sy])
            if answer < cur:
                answer = cur
            num[sx][sy] = temp
        sx += dx[d]
        sy += dy[d]

    return answer

num = [[0]*n for _ in range(n)]
direction = [[0]*n for _ in range(n)]

for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(n):
        num[i][j] = temp[2*j]
        direction[i][j] = temp[2*j+1]
        direction[i][j] -= 1
ans = num[0][0]
num[0][0] = 0
ans += go(num, direction, 0, 0, direction[0][0])
print(ans)