# 나무 재테크
# 3중 그래프 생성 숙달 필요
# heapq.heappush함수의 O(logn), n = 라스트 길이의 시간복잡도를 가진다.
# 위 함수를 아래 코드처럼 남발하게 되면 시간 비용이 증가하게 되니 최대한 줄이는게 중요하다.
# 이 문제같은경우는 나무가 양분을 흡수하기 전에 작은 나무순으로 정렬을 한번만 하면된다.
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

    # 봄 + 여름
    for i in range(n):
        for j in range(n):
            trees = b[i][j]
            plus = 0
            n_trees = []
            if trees:
                # 추가 영양분
                while trees:
                    tree = heapq.heappop(trees)
                    
                    # 양분이 적은 경우
                    if tree > c[i][j]:
                        plus += tree // 2
                    
                    else:
                        c[i][j] -= tree
                        heapq.heappush(n_trees,tree+1)
            
            c[i][j] += plus
            b[i][j] = n_trees

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
                            heapq.heappush(b[nx][ny],1)
    
    # 겨울
    for i in range(n):
        for j in range(n):
            c[i][j] += a[i][j]

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(b[i][j])

print(ans)




