#스타트링크

from collections import deque

F, S, G, U, D = map(int,input().split())

dx = [U,-D]
dist = [-1] * (F + 1)
dq = deque()

dq.append(S)
dist[S] = 0

while dq:
    x = dq.popleft()

    for i in range(2):
        nx = x + dx[i]
        if 0 < nx <= F and dist[nx] == -1:
            dq.append(nx)
            dist[nx] = dist[x] + 1

print('use the stairs' if dist[G] == -1 else dist[G])
