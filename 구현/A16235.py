# 나무 재테크
import heapq

n, m, k = map(int, input().split())

# 양분 그래프
a = [list(map(int,input().split())) for _ in range(n)]

# 나무 위치 그래프
b = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    heapq.heappush(b[x-1][y-1],z)
    

# 밭 그래프
c = [[5] * n for _ in range(n)]

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

for _ in range(k):

    # 봄 + 여름 + 겨울
    for i in range(n):
        for j in range(n):
            b[i][j].sort()
            plus = 0
            n_trees = []
           
            for tree in b[i][j]:
                # 양분이 적은 경우
                if tree > c[i][j]:
                    plus += tree // 2
                
                else:
                    c[i][j] -= tree
                    n_trees.append(tree+1)
            
            c[i][j] += plus
            b[i][j] = n_trees
            c[i][j] += a[i][j]

    # 가을
    for i in range(n):
        for j in range(n):
            trees = b[i][j]

            for tree in trees:
                # 5의 배수이면 번식
                if tree % 5 == 0:

                    for k in range(8):
                        nx, ny = i + dx[k], j + dy[k]

                        if 0 <= nx < n and 0 <= ny < n:
                            b[nx][ny].append(1)
            

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(b[i][j])

print(ans)




