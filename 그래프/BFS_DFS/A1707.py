#이분 그래프

import sys
sys.setrecursionlimit(10**6)
def DFS(x,c):
    visited[x] = c
    for i in g[x]:
        if(visited[i] == 3):
            if(DFS(i,3-visited[x]) == False):
                return False
        elif visited[i] == visited[x]:
            return False
    return True
T = int(input())

for _ in range(T):
    V, E = map(int, sys.stdin.readline().split())
    g = [[] for i in range(V+1)]
    visited = [3 * 1 for i in range(V+1)]
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        g[u].append(v)
        g[v].append(u)
    
    result = True
    for i in range(1,V+1):
        if visited[i] == 3:
            tmp = DFS(i,1)
            if tmp == False:
                result = False
    print("YES" if result else "NO")



