# 너비 우선 탐색
from collections import deque 
graph = []
que = deque()
n,m = map(int,input().split())
for i in range(n):
    graph.append(list(map(int,input().split())))
def check_graph():
    global graph, que
    tmp = que.popleft()
    #동
    if tmp[1] < m-1:
        if graph[tmp[0]][tmp[1]+1] == 0:
            graph[tmp[0]][tmp[1]+1] = 1
            que.append([tmp[0],tmp[1]+1])
    #서
    if tmp[1] > 0:
        if graph[tmp[0]][tmp[1]-1] == 0:
            graph[tmp[0]][tmp[1]-1] = 1
            que.append([tmp[0],tmp[1]-1])
    #남
    if tmp[0] < n-1:
        if graph[tmp[0]+1][tmp[1]] == 0:
            graph[tmp[0]+1][tmp[1]] = 1
            que.append([tmp[0]+1,tmp[1]])
    #북
    if tmp[0] > 0:
        if graph[tmp[0]-1][tmp[1]] == 0:
            graph[tmp[0]-1][tmp[1]] = 1
            que.append([tmp[0]-1,tmp[1]])
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result += 1
            que.append([i,j])
            graph[i][j] = 1
            while(len(que) != 0):
                check_graph()
print(result)
