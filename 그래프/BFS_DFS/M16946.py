#벽부수고 이동하기4
#같은 리스트(A)를 다른 두개의 리스트(B,C)에 대입하면 B에 있는 A리스트가 바뀌면 C에 있는 A리스트도 바뀐다.
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
result_graph = [[] for _ in range(N)]
wall = []
not_wall = []
dic = {}
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for i in range(N):
    tmp = []
    line = input()
    for j in range(M):
        if line[j] == '1':
            wall.append((i,j))
            tmp.append(1)
            graph[i].append(1)
            result_graph[i].append(1)
        else:
            not_wall.append((i,j))
            graph[i].append(0)
            result_graph[i].append(0)

count = 2
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            block = 1
            dq = deque()
            dq.append((i,j))
            graph[i][j] = count
            while dq:
                x, y = dq.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx >=0 and nx < N and ny >=0 and ny < M and graph[nx][ny] == 0:
                        block += 1
                        graph[nx][ny] = count
                        dq.append((nx,ny))
            dic[count] = block
            count += 1
            
for x, y in wall:
    if graph[x][y] == 1:
        block_count = 1
        collect = set()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and nx < N and ny >= 0 and ny < M and graph[nx][ny] > 1:
                collect.add(graph[nx][ny])
        for i in collect:
            block_count += dic[i]
        result_graph[x][y] = block_count

for i in range(N):
    for j in range(M):
        print(result_graph[i][j],end='')
    print('')