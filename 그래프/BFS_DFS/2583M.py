#영역 구하기
import sys
sys.setrecursionlimit(10**7)
M,N,K = (map(int,sys.stdin.readline().split()))
li = [list(map(int,sys.stdin.readline().split())) for _ in range(K)]
hang = [[0] * N for _ in range(M)]

for x0, y0, x1, y1 in li:
    for j in range(x0,x1):
        for k in range(y0,y1):
            hang[k][j] = 1
            
def DFS(x,y,countli):
    if(x < 0 or x >= M or y < 0 or y >= N):
        return
    else:
        if(hang[x][y] == 0):
            hang[x][y] = 1
            countli.append([x,y])
            DFS(x+1,y,countli)
            DFS(x-1,y,countli)
            DFS(x,y+1,countli)
            DFS(x,y-1,countli)
        
count = 0
result = []
for i in range(N):
    for j in range(M):
        countli = []
        if(hang[j][i] == 0):
            count += 1
            DFS(j,i,countli)
        if len(countli) != 0:
            result.append(len(countli))
result = sorted(result)
print(count)
for i in result:
    print(i,end=" ")