# 원판 돌리기
import copy 

def rotate(k, d, x):
    if d == 0: # 시계 방향
        for i in range(n):
            if (i+1) % x == 0:
                tmp = [0] * m
                for j in range(m):
                    index = (j + k) % m
                    tmp[index] = g[i][j]
                g[i] = tmp
    elif d == 1:
        for i in range(n):
            if (i+1) % x == 0:
                tmp = [0] * m
                for j in range(m):
                    index = (j - k) % m
                    tmp[index] = g[i][j]
                g[i] = tmp
        


n, m, t = map(int,input().split())

g = [list(map(int,input().split())) for _ in range(n)]

# 원판 돌리기
for _ in range(t):
    x, d, k = map(int,input().split())

    # x 배수 회전
    rotate(k,d,x)
    new_g = copy.deepcopy(g)
    erases = False
    for i in range(n):
        cnt = 0

        # 원판에 수가 남아 있는지 확인
        for j in range(m):
            if g[i][j] == 0:
                cnt += 1
            
            if cnt == m:
                break        
        
        # 인접 지우기
        for j in range(m):
            if g[i][j] == 0:
                continue
            
            # 원판 인접
            if i+1 < n and g[i][j] == g[i+1][j]:
                new_g[i][j] = 0
                new_g[i+1][j] = 0
                erases = True
           
            # 좌우 인접
            r = (j+1) % m

            if g[i][j] == g[i][r]:
                new_g[i][r] = 0
                new_g[i][j] = 0
                erases = True
        
    g = new_g

    if not erases:
        amount = 0
        cnt = 0
        for i in range(n):
            for j in range(m):
                if g[i][j] > 0:
                    amount += g[i][j]
                    cnt += 1
        
        if amount == 0:
            break
        avg = amount / cnt

        for i in range(n):
            for j in range(m):
                if 0 < g[i][j] < avg:
                    g[i][j] += 1
                elif g[i][j] > avg:
                    g[i][j] -= 1

ans = 0

for i in range(n):
    for j in range(m):
        ans += g[i][j]

print(ans)