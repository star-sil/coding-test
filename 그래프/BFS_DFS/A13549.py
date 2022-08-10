#숨바꼭질 3
#0-1 BFS
#가중치가 0인 간선과 1인 간선이 갈수있는 공통된 정점이 있을때 0으로 가는것이 빠르므로 0인간선을 우선으로 큐 앞에 넣는다.
import sys
from collections import deque

N, K = map(int, input().split())
position = [-1 for i in range(200000)]
dq = deque()

dq.append(N)
position[N] = 0

while dq:
    print(dq)
    x = dq.popleft()
    if x == 17:
        break
    
    if x * 2 < 200000 and position[x*2] == -1:
        dq.appendleft(x*2)
        position[x*2] = position[x]
    if x - 1 >= 0 and position[x-1] == -1:
        dq.append(x-1)
        position[x-1] = position[x] + 1
    if x + 1 < 200000 and position[x+1] == -1:
        dq.append(x+1)
        position[x+1] = position[x] + 1
    


print(position[K])




