#뱀과 사다리 게임

from collections import deque
graph = [i for i in range(101)]
dist = [-1 for i in range(101)]

N, M = map(int, input().split())
for _ in range(N + M):
    f,t = map(int,input().split())
    graph[f] = t

dq = deque()
dq.append(1)
dist[1] = 0

while dq:
    block = dq.popleft()
    
    for i in range(1,7):
        if block + i <= 100:
            next_block = graph[block + i]
            if dist[next_block] == -1:
                dist[next_block] = dist[block] + 1
                dq.append(next_block)

print(dist[100])        





