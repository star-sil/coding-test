#숨바꼭질
import sys
from collections import deque
sys.setrecursionlimit(10**7)

N, K = map(int,input().split())
visited = [False for i in range(200000)]
graph = [0 for i in range(200000)]

dq = deque()
dq.append(N)
visited[N] = True

while dq:
    x = dq.popleft()
    for i in [x+1,x-1,2*x]:
        if(i < 200000 and i >= 0):
            if visited[i] == False:
                dq.append(i)
                visited[i] = True
                graph[i] = graph[x] + 1

print(graph[K])