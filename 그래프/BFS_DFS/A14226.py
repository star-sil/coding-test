#이모티콘
import sys
from collections import deque

dq = deque()

S = int(input())
dist = [[-1] * (S*2) for i in range(S*2)]
dist[1][0] = 0
dq.append([1,0])

while dq:
    e, c = dq.popleft()
    if dist[e][e] == -1:
        dist[e][e] = dist[e][c] + 1
        dq.append([e,e])
    if (e + c < S*2) and dist[e+c][c] == -1:
        dist[e+c][c] = dist[e][c] + 1
        dq.append([e+c,c])
    if (e - 1 > -1) and dist[e-1][c] == -1:
        dist[e-1][c] = dist[e][c] + 1
        dq.append([e-1,c])

result = -1
for i in range(S*2):
    if dist[S][i] != -1:
        if result == -1 or result > dist[S][i]:
            result = dist[S][i]
print(result)



    
    