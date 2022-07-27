#유기능 배추 #116ms
import sys
sys.setrecursionlimit(10**6)
T = int(sys.stdin.readline())
index = []
for i in range(T):
    tmp = []
    M,N,K = map(int,sys.stdin.readline().split())
    for i in range(N):
        tmp.append([0 for _ in range(M)])
    for i in range(K):
        n,m = map(int,sys.stdin.readline().split())
        tmp[m][n] = 1
    index.append(tmp)

def DFS(i,row,col):
    if row >= 0 and row < len(index[i]) and col < len(index[i][0]) and col >= 0 and index[i][row][col] == 1:
        index[i][row][col] = 0
        DFS(i,row+1,col)
        DFS(i,row-1,col)
        DFS(i,row,col+1)
        DFS(i,row,col-1)
     
#DFS
for i in range(T):
    count = 0
    for row in range(len(index[i])):
        for col in range(len(index[i][0])):
            if index[i][row][col] == 1:
                count += 1
                DFS(i,row,col)
    print(count)