#로봇 청소기
import sys
from collections import deque

def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True

def bfs(graph,sx,sy):
    dist = [[-1] * w for _ in range(h)]
    dq = deque()
    dq.append((sx,sy))
    dist[sx][sy] = 0
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and dist[nx][ny] == -1 and graph[nx][ny] != 'x':
                dist[nx][ny] = dist[x][y] + 1
                dq.append((nx,ny))
    return dist

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    graph = [list(sys.stdin.readline()) for _ in range(h)]
    dx, dy = [0,0,-1,1], [1,-1,0,0]
    b = [(0,0)]


    for i in range(h):
        for j in range(w):
            if graph[i][j] == 'o':
                b[0] = (i,j)
            elif graph[i][j] == '*':
                b.append((i,j))
    l = len(b)
    d = [[0]*l for _ in range(l)]
    ok = True
    for i in range(l):
        dist = bfs(graph,b[i][0],b[i][1])
        for j in range(l):
            d[i][j] = dist[b[j][0]][b[j][1]]
            if d[i][j] == -1:
                ok = False
    if not ok:
        print(-1)
        continue

    p = [i+1 for i in range(l-1)]
    ans = -1

    while True:
        now = d[0][p[0]]
        for i in range(l-2):
            now += d[p[i]][p[i+1]]
        if ans == -1 or ans > now:
            ans = now
        if not next_permutation(p):
            break

    print(ans)