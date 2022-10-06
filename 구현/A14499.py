#주사위 굴리기
#주사위 면 기준으로 상하좌우 마주보는 면은 바뀐다.
#전개도 위치를 기반으로 동, 서, 남, 북 이동에 따라 주사위 값을 배정한다.

def change_dice(pos,f):
    dice = [0] * 6
    if pos == 1: #동
        dice[1] = f[2]
        dice[2] = f[3]
        dice[3] = f[5]
        dice[5] = f[1]
        dice[4] = f[4]
        dice[0] = f[0]
    elif pos == 2: #서
        dice[1] = f[5]
        dice[2] = f[1]
        dice[3] = f[2]
        dice[5] = f[3]
        dice[0] = f[0]
        dice[4] = f[4]
    elif pos == 3: #남
        dice[0] = f[2]
        dice[2] = f[4]
        dice[4] = f[5]
        dice[5] = f[0]
        dice[1] = f[1]
        dice[3] = f[3]
    elif pos == 4: #북
        dice[0] = f[5]
        dice[2] = f[0]
        dice[4] = f[2]
        dice[5] = f[4]
        dice[1] = f[1]
        dice[3] = f[3]
    return dice
    
f = [0] * 6
dx,dy = [0,0,-1,1], [1,-1,0,0] # 동 서 북 남
a = []
n,m,x,y,k = map(int,input().split())
for _ in range(n):
    a.append(list(map(int,input().split())))

orderList = list(map(int,input().split()))

for i in orderList:
    nx,ny = x + dx[i-1], y + dy[i-1]
    if 0 <= nx < n and 0 <= ny < m:
        f = change_dice(i,f)  # 다음 주사위 전개도
        if a[nx][ny] == 0: # 이동한 칸에 쓰여있는 수가 0이면 주사위 바닥면에 쓰여있는 수가 칸에 복사
            a[nx][ny] = f[2]
        else: # 이동한 칸에 쓰여있는 수가 0이 아니면 주사위 바닥면에 쓰여있는 수가 이동한 칸에 복사
            f[2] = a[nx][ny]
            a[nx][ny] = 0 # 바닥면은 다시 0이된다.
        x,y = nx,ny
        
        print(f[5]) #주사위 윗면 값 출력
        



        
