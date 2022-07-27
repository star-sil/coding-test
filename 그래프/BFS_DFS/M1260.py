# DFS와 BFS
from collections import deque

N, M ,V= map(int, input().split())

g = [[] * i for i in range(N+1)]
visited1 = [False * i for i in range(N+1)]
visited2 = [False * i for i in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    g[v1].append(v2)
    g[v2].append(v1)

for i in range(1,N+1):
    g[i].sort()

dList = []
def dfs(x):
    if visited1[x] == False:
        visited1[x] = True
        dList.append(x)
        for i in g[x]:
            dfs(i)

dq = deque()
bList = []
def bfs(x):
    while len(dq) > 0:
        x = dq.popleft()
        bList.append(x)
        for i in g[x]:
            if visited2[i] == False:
                visited2[i] = True
                dq.append(i)

dfs(V)
dq.append(V)
visited2[V] = True
bfs(V)

for i in dList:
    print(i,end=" ")
print()
for i in bList:
    print(i,end=" ")