#영역 구하기
"""더 간편하게 짰다 + 재귀함를 이용한 DFS를 통해 넓이도 구할 수 있다는 것을 명심하자!!"""
import sys
sys.setrecursionlimit(10**7)
M,N,K = (map(int,sys.stdin.readline().split()))
li = [list(map(int,sys.stdin.readline().split())) for _ in range(K)]
hang = [[0] * N for _ in range(M)]

for x0, y0, x1, y1 in li:
    for j in range(x0,x1):
        for k in range(y0,y1):
            hang[k][j] = 1
            
def DFS(x,y):
    global count
    if(x < 0 or x >= M or y < 0 or y >= N):
        return
    else:
        if(hang[x][y] == 0):
            hang[x][y] = 1
            count += 1
            DFS(x+1,y)
            DFS(x-1,y)
            DFS(x,y+1)
            DFS(x,y-1)
        
count = 0
result = []
for i in range(N):
    for j in range(M):
        countli = []
        if(hang[j][i] == 0):
            count = 0
            DFS(j,i)
            result.append(count)

result = sorted(result)
print(len(result))
for i in result:
    print(i,end=" ")