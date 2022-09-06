#BFS 스페셜 저지

from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(N-1):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
resultList = deque(map(int,input().split()))
li = {}
for i in range(N):
    v = resultList[i]
    li[v] = i

dq = deque()
result = deque()
dq.append(1)
result.append(1)
visited[1] = True
while dq:
    v = dq.popleft()
    sort = []
    for i in graph[v]:
        sort.append((li[i],i))
    sort.sort()
    for i,j in sort:
        if visited[j] == False:
            visited[j] = True
            dq.append(j)
            result.append(j)

ans = 1
for i in range(N-1):
    if result[i] != resultList[i]:
        ans = 0

print(ans)