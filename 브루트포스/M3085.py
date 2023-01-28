# 사탕 게임
# 공백 없는 문자열 자르기 => list(문자열)
# 리스트 원소 교환 => list[a], list[b] = list[b], list[a]
# 상하좌우 다 할 필요없다. => 하,우 방향으로 탐색을 하면 원소의 상,좌 방향은 이전 원소순서에서 골랐기 때문

n = int(input())

candy = [list(input()) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = 0

for i in range(n):
    for j in range(n):
        
        # 인접한 두칸 찾기
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if candy[i][j] != candy[nx][ny]:
                    candy[i][j], candy[nx][ny] = candy[nx][ny], candy[i][j]

                    # 먹을 수 있는 사탕의 최대 갯수 구하기
                    for x in range(n):
                        tmp = 1
                        for y in range(n-1):
                            if candy[x][y] != candy[x][y+1]:
                                ans = max(ans,tmp)
                                tmp = 1
                                continue
                            tmp += 1
                        ans = max(ans,tmp)

                    for y in range(n):
                        tmp = 1
                        for x in range(n-1):
                            if candy[x][y] != candy[x+1][y]:
                                ans = max(ans,tmp)
                                tmp = 1
                                continue
                            tmp += 1
                        ans = max(ans,tmp)
                        
                    candy[i][j], candy[nx][ny] = candy[nx][ny], candy[i][j]

print(ans)