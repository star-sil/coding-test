n, m, count = map(int, input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

sharks = [list(map(int,input().split())) for _ in range(n)] # 상어의 위치
smell = [[0] * n for _ in range(n)] # 냄새 정보
smellCount = [[0] * n for _ in range(n)] # 냄새 유지 카운트
ndirect = list(map(int,input().split())) # 상어의 현재 방향
directions = [[list(map(int,input().split())) for _ in range(4)] for _ in range(m)] # 상어의 방향 우선 순위


for t in range(1001):

    # 1번 상어만 격자에 남아있는지 확인
    finish = True
    for i in range(n):
        for j in range(n):
            if sharks[i][j] > 1:
                finish = False
    # 찾을 시 종료
    if finish:
        print(t)
        exit()

    # 냄새 뿌리기
    for i in range(n):
        for j in range(n):
            if sharks[i][j] > 0:
                smell[i][j] = sharks[i][j]
                smellCount[i][j] = count
    
    # 상어 이동
    newSharks = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if sharks[i][j] > 0:
                d = ndirect[sharks[i][j]-1] # 현재 방향

                # 냄새 없는 방향 찾기
                find = False
                nextDirects = directions[sharks[i][j]-1][d-1]
                for k in range(4):  
                    nd = nextDirects[k]
                    nx, ny = i + dx[nd-1], j + dy[nd-1]

                    if 0 <= nx < n and 0 <= ny < n:
                        # 냄새가 없는 칸
                        if smell[nx][ny] == 0:
                            find = True
                            # 자신보다 큰 번호 상어가 있을때 
                            if newSharks[nx][ny] > sharks[i][j] or newSharks[nx][ny] == 0:
                                newSharks[nx][ny] = sharks[i][j]
                                ndirect[sharks[i][j]-1] = nd
                            break
                
                # 냄새없는 곳 없으면 자기 자신 냄새 있는 곳가기
                if not find:
                    for k in range(4):
                        nd = nextDirects[k]
                        nx, ny = i + dx[nd-1], j + dy[nd-1]

                        if 0 <= nx < n and 0 <= ny < n:
                            if smell[nx][ny] == sharks[i][j]:
                                newSharks[nx][ny] = sharks[i][j]
                                ndirect[sharks[i][j]-1] = nd
                                break
    sharks = newSharks   
                
    # 냄새 유지시간 끝낸 곳 없애기
    for i in range(n):
        for j in range(n):          

            if smellCount[i][j] > 0:
                smellCount[i][j] -= 1
                if smellCount[i][j] == 0:
                    smell[i][j] = 0

print(-1)