#알고스팟
"""
이 문제는 내가 잘 못 생각했다. 최단경로를 찾아야 하지만 단순히 깊이 우선탐색으로 문제를 해결하려했다....
심지어 dfs도 잘 못 구현했다...
앞으로 최단경로를 구현할때는 bfs알고리즘으로 읽자!!
"""
import sys
sys.setrecursionlimit(10**7)
N, M = map(int, sys.stdin.readline().split())
Miro = [list(map(int,sys.stdin.readline())) for _ in range(M)]
count = 0
li = []
def DFS(x,y,tx,ty):
    global count
    if(x == tx-1 and y == ty-1):
        print('====',count)
        li.append(count)
        count = 0
    elif(x < 0 or y < 0 or x > tx-1 or y > ty-1):
        pass
    else:
        print(x,y)
        if(Miro[x][y] == 1):
            count += 1
        DFS(x+1,y,tx,ty)
        DFS(x,y+1,tx,ty)
DFS(0,0,M,N)
print(li)


