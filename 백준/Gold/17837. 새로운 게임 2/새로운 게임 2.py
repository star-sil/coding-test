# 새로운 게임 2

def change_direction(d):
    if d == 0 or d == 1:
        return 1 - d
    return 5 - d


n, m = map(int,input().split())

g = [list(map(int,input().split())) for _ in range(n)]
p = [[[] for _ in range(n)] for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(m):
    r,c,d = map(int,input().split())
    p[r-1][c-1].append([i+1,d-1])

for t in range(1,1001):

    # 번호 순서대로 말 찾기
    for i in range(1,m+1):
        go = False
        for j in range(n):
            for k in range(n):
                for h in range(len(p[j][k])):
                    
                    # 말을 찾은 경우
                    if p[j][k][h][0] == i:
                        horses = p[j][k][h:]
                        go = True
                        num, d = p[j][k][h]
                        nx, ny = j + dx[d], k + dy[d]

                        # 범위 안이라면
                        if 0 <= nx < n and 0 <= ny < n:

                            # 흰색
                            if g[nx][ny] == 0:
                                p[nx][ny] += horses
                                p[j][k] = p[j][k][:h]
                            
                            # 빨간색
                            elif g[nx][ny] == 1:
                                horses.reverse()
                                p[nx][ny] += horses
                                p[j][k] = p[j][k][:h]

                            # 파란색
                            elif g[nx][ny] == 2:
                                d = change_direction(d)
                                nx, ny = j + dx[d], k + dy[d]
                                p[j][k][h][1] = d
                                horses[0][1] = d
                                
                                # 움직일 수 있는 경우
                                if 0 <= nx < n and 0 <= ny < n:
                                    
                                    # 흰색인 경우
                                    if g[nx][ny] == 0:
                                        p[nx][ny] += horses
                                        p[j][k] = p[j][k][:h]
                                    # 빨간색인 경우
                                    elif g[nx][ny] == 1:
                                        horses.reverse()
                                        p[nx][ny] += horses
                                        p[j][k] = p[j][k][:h]

                        else: # 범위 벗어나는 경우

                            # 방향 전환
                            d = change_direction(d)
                            nx, ny = j + dx[d], k + dy[d]
                            p[j][k][h][1] = d
                            horses[0][1] = d

                            # 움직일 수 있는 경우
                            if 0 <= nx < n and 0 <= ny < n:

                                # 흰색인 경우
                                if g[nx][ny] == 0:
                                    p[nx][ny] += horses
                                    p[j][k] = p[j][k][:h]

                                # 빨간색인 경우
                                elif g[nx][ny] == 1:
                                    horses.reverse()
                                    p[nx][ny] += horses
                                    p[j][k] = p[j][k][:h]
                        break
                if go:
                    break
            if go:
                break
    
        # 말 하나가 움직일때마다 종료 조건 충족 확인 (순간 조건이기 때문)
        for j in range(n):
            for k in range(n):
                
                # 말이 4개면 종료
                if len(p[j][k]) >= 4:
                    print(t)
                    exit()
        
print(-1)