# 청소년 상어
# 물고기 움직이는 부분에서 시간 많이 잡아먹음 -> 방향 인덱스 초기 셋팅 -1 안한것이 원인
# 상위에서 아직 사용중인 변수는 변경하지 않는다.
import copy

g = []

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

for i in range(4):
    l = list(map(int, input().split()))
    tmp = []
    for j in range(len(l)):
        if j % 2 == 0:
            tmp.append([l[j],l[j+1]-1])
    g.append(tmp)

# 상어 출발
eat = g[0][0][0]
g[0][0][0] = 17 # 상어번호


def go(shark,ng):
    # 물고기 번호 찾기
    for i in range(1,17):
        find = False
        for j in range(4):
            for k in range(4):
                if ng[j][k][0] == i:
                    # 움직일 수 있는 곳 찾기
                    for l in range(8):
                        nd = (ng[j][k][1] + l) % 8
                        nx, ny = j + dx[nd], k + dy[nd]
                        # 갈 수 있다면 가기
                        if 0 <= nx < 4 and 0 <= ny < 4 and ng[nx][ny][0] != 17:
                            # 가는 곳에 물고기가 있다면 위치 교환
                            tmp = ng[j][k] 
                            ng[j][k] = ng[nx][ny]
                            ng[nx][ny] = [tmp[0],nd]
                            #ng[j][k], ng[nx][ny] = ng[nx][ny], [ng[j][k][0],nd]
                            find = True
                            break
                if find:
                    break
            if find:
                break

    # 상어 움직이기
    ans = 0
    nx, ny = shark[0], shark[1]
    for i in range(1,4):
        nx += dx[shark[2]]
        ny += dy[shark[2]]

        # 움직일 수 있는 칸이 범위 안
        if 0 <= nx < 4 and 0 <= ny < 4:
            if 0 < ng[nx][ny][0] < 17: # 물고기 있는 경우
                tg = copy.deepcopy(ng)
                tg[nx][ny] = [17,ng[nx][ny][1]]
                tg[shark[0]][shark[1]] = [0,0]
                cur = ng[nx][ny][0] + go([nx,ny,ng[nx][ny][1]],tg)

                if ans < cur:
                    ans = cur

    return ans

eat += go([0,0,g[0][0][1]],g)
print(eat)


                        

