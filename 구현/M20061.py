# 모노미노도미노 2
# 제거순서 열이나 행이 가득찬거 지우기 -> 연한칸
# 가득찬거 확인, 지우기, 내리기

dx = [0, 0, 1]
dy = [0, 1, 0]

n = int(input())

blocks = [list(map(int,input().split())) for _ in range(n)]

green = [[False] * 4 for _ in range(6)]
blue = [[False] * 6 for _ in range(4)]
score = 0

for block in blocks:
    t,x,y = block

    tx,ty = x + dx[t-1], y + dy[t-1]
    
    # 블록 쌓기 초록색 & 파란색
    gx = 0
    gtx = tx - x
    for _ in range(6):
        if 0 <= gx + 1 < 6 and 0 <= gtx + 1 < 6:
            if not green[gx+1][y] and not green[gtx+1][ty]:
                gx += 1
                gtx += 1
    green[gx][y] = True
    green[gtx][ty] = True

    bty = ty - y
    by = 0
    for _ in range(6):
        if 0 <= by + 1 < 6 and 0 <= bty + 1 < 6:
            if not blue[x][by+1] and not blue[tx][bty+1]:
                by += 1
                bty += 1
    blue[x][by] = True
    blue[tx][bty] = True

    # 블록 지우기
    for i in range(2,6):
        clear = True
        for j in range(4):
            if green[i][j] == False:
                clear = False

        if clear:
            score += 1
            for j in range(4):
                green[i][j] = False
            
            for j in range(i-1,-1,-1):
                for k in range(4):
                    green[j+1][k] = green[j][k]
    
    for i in range(2,6):
        clear = True
        for j in range(4):
            if blue[j][i] == False:
                clear = False

        if clear:
            score += 1
            for j in range(4):
                blue[j][i] = False
            
            for j in range(i-1,-1,-1):
                for k in range(4):
                    blue[k][j+1] = blue[k][j]
                    

    # 초록색 연한색 지우기
    cnt = 0
    for i in range(2):
        for j in range(4):
            if green[i][j]:
                cnt += 1
                break
    
    for i in range(cnt):
        for j in range(4,-1,-1):
            for k in range(4):        
                green[j+1][k] = green[j][k]
                green[j][k] = False

    # 파란색 연한색 지우기
    cnt = 0
    for i in range(2):
        for j in range(4):
            if blue[j][i]:
                cnt += 1
                break
    
    for i in range(cnt):
        for j in range(4,-1,-1):
            for k in range(4):
                blue[k][j+1] = blue[k][j]
                blue[k][j] = False
                
print(score)

ans = 0
for i in range(6):
    for j in range(4):
        if green[i][j]:
            ans += 1
            
for i in range(4):
    for j in range(6):
        if blue[i][j]:
            ans += 1

print(ans)