import sys
from collections import deque
from typing import ValuesView
sys.setrecursionlimit(10**6)
dfs = []; bfs = []
n,m,v = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i = i.sort()

def DFS(v,graph,visited):
    visited[v] = True
    dfs.append(str(v))
    for i in graph[v]:
        if not visited[i]:
            DFS(i,graph,visited)

visited2 = [False for _ in range(n+1)]
def BFS(v,graph,visited):
    que = deque([v])
    visited[v] = True
    while que:
        pop_v = que.popleft()
        bfs.append(str(pop_v))
        visited[pop_v] = True
        for i in graph[pop_v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True

DFS(v,graph,visited)
BFS(v,graph,visited2)
print(' '.join(dfs))
print(' '.join(bfs))