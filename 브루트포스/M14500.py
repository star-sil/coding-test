# 테트로미노
# 모든 도형의 경우의 수를 구하고 풀면 된다.

t = [
    [(0,1),(0,2),(0,3)],
    [(1,0),(2,0),(3,0)],

    [(0,1),(1,0),(1,1)],

    [(1,0),(2,0),(2,1)],
    [(1,0),(1,-1),(1,-2)],
    [(0,1),(1,1),(2,1)],
    [(1,0),(0,1),(0,2)],
    [(1,0),(2,0),(2,-1)],
    [(1,0),(1,1),(1,2)],
    [(0,-1),(1,-1),(2,-1)],
    [(0,1),(0,2),(1,2)],

    [(1,0),(1,1),(2,1)],
    [(0,-1),(1,-1),(1,-2)],
    [(1,0),(1,-1),(2,-1)],
    [(0,1),(1,1),(1,2)],

    [(0,1),(0,2),(1,1)],
    [(1,0),(1,-1),(1,1)],
    [(1,0),(2,0),(1,1)],
    [(1,0),(2,0),(1,-1)]
]

n, m = map(int,input().split())

a = [list(map(int,input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):

        # 도형 넣을 수 있는지 확인
        for k in t:
            score = a[i][j]
            possible = True
            for dx, dy in k:
                nx, ny = i + dx, j + dy
                
                if 0 <= nx < n and 0 <= ny < m:
                    score += a[nx][ny]
                else:
                    possible = False
            
            if possible:
                ans = max(ans,score)

print(ans)