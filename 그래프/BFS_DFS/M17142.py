#연구소 3
from collections import deque

n,m = map(int,input().split())
pos = []
a = []
dx, dy = [0,0,-1,1], [1,-1,0,0]

def combination(arr, n):
    result =[] 

    if n == 0: 
        return [[]]

    for i in range(0, len(arr)): 
        elem = arr[i] 
        rest_arr = arr[i + 1:] 
        for C in combination(rest_arr, n-1): 
            result.append([elem]+C) 
              
    return result

def bfs(virus):
    dq = deque()
    dist = [[-1] * n for _ in range(n)]

    for v in virus:
        dq.append((v[0],v[1]))
        dist[v[0]][v[1]] = 0
    
    while dq:
        x, y= dq.popleft()
        for i in range(4):
            nx, ny= x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == 1 or dist[nx][ny] >= 0:
                    continue
                dist[nx][ny] = dist[x][y] + 1
                dq.append((nx,ny))

    time = 0
    for i in range(n):
        for j in range(n):
            if dist[i][j] == -1 and a[i][j] == 0:
                return -1
            if a[i][j] == 2:
                continue
            else:
                time = max(time,dist[i][j])
    return time


for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(len(tmp)):
        if tmp[j] == 2:
            pos.append((i,j))
    a.append(tmp)

viruses = combination(pos,m)

ans = -1
for vir in viruses:
    result = bfs(vir)
    if ans == -1:
        ans = result
    else:
        if result != -1:
            ans = min(ans,result)
print(ans)