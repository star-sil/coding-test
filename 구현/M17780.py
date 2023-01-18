# 새로운 게임 (다시 풀어보기)
# 굳이 deque를 사용하지 않아도 된다.
# 왜냐하면 말의 동작 순서는 바뀌지 않는다.
# 그냥 말들을 순환하면서 말이 맨 밑에 있는 경우 제시한 경우로 말을 움직이면 된다.
# 3중 리스트 구현 필요
# 파란색 함정 주의 반대편으로 방향 바꿔서 움질일때 움직일 칸의 색깔 다시 고려해야함

def change_direction(d):
    if d == 0 or d == 1:
        return 1 - d
    return 5 - d


n, h = map(int,input().split())

g = [list(map(int,input().split())) for _ in range(n)]
p = [[[] for _ in range(n)] for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(h):
    r,c,d = map(int,input().split())
    p[r-1][c-1].append([i+1,d-1])

turn = 0
for _ in range(1001):

    for j in range(n):
        for k in range(n):
            # 말이 4개면 종료
            if len(p[j][k]) >= 4:
                print(turn)
                exit()

    # 번호 순서대로 말 찾기
    for i in range(1,h+1):
        go = False

        for j in range(n):
            for k in range(n):
                
                # 말이 맨 밑에 있는 경우
                if len(p[j][k]) > 0 and i == p[j][k][0][0]:
                    go = True
                    num, d = p[j][k][0]

                    nx, ny = j + dx[d], k + dy[d]
                    horses = p[j][k]

                    # 범위 안이라면
                    if 0 <= nx < n and 0 <= ny < n:

                        # 흰색
                        if g[nx][ny] == 0:
                            
                            #print('b: ',p[j][k],p[nx][ny])
                            p[nx][ny] += horses
                            p[j][k] = []
                            #print('a: ',p[nx][ny])
                        
                        # 빨간색
                        elif g[nx][ny] == 1:

                            horses.reverse()
                            p[nx][ny] += horses
                            p[j][k] = []

                        # 파란색
                        elif g[nx][ny] == 2:

                            d = change_direction(d)
                            nx, ny = j + dx[d], k + dy[d]
                            horses[0][1] = d
                            
                            # 움직일 수 있는 경우
                            if 0 <= nx < n and 0 <= ny < n:
                                
                                # 흰색인 경우
                                if g[nx][ny] == 0:
                                    p[nx][ny] += horses
                                    p[j][k] = []
                                # 빨간색인 경우
                                elif g[nx][ny] == 1:
                                    horses.reverse()
                                    p[nx][ny] += horses
                                    p[j][k] = []



                    else: # 범위 벗어나는 경우

                        # 방향 전환
                        d = change_direction(d)
                        nx, ny = j + dx[d], k + dy[d]
                        horses[0][1] = d

                        # 움직일 수 있는 경우
                        if 0 <= nx < n and 0 <= ny < n:
                            
                            # 흰색인 경우
                            if g[nx][ny] == 0:
                                p[nx][ny] += horses
                                p[j][k] = []
                            # 빨간색인 경우
                            elif g[nx][ny] == 1:
                                horses.reverse()
                                p[nx][ny] += horses
                                p[j][k] = []
                if go:
                    break
            
            if go:
                break
    turn += 1

        
print(-1)
