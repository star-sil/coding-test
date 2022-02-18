from collections import deque
graph = []
que = deque([[0,0]])
n,m = map(int,input().split())
for i in range(n):
    graph.append(list(map(int,input())))

def bfs():
    global graph, que
    tmp = que.popleft()
    if tmp[1] < m - 1:
        if graph[tmp[0]][tmp[1]+1] == 1:
            graph[tmp[0]][tmp[1]+1] = graph[tmp[0]][tmp[1]] + 1
            que.append([tmp[0],tmp[1]+1])
    if tmp[1] > 0:
        if graph[tmp[0]][tmp[1]-1] == 1:
            graph[tmp[0]][tmp[1]-1] = graph[tmp[0]][tmp[1]] + 1
            que.append([tmp[0],tmp[1]-1])
    if tmp[0] < n - 1:
        if graph[tmp[0]+1][tmp[1]] == 1:
            graph[tmp[0]+1][tmp[1]] = graph[tmp[0]][tmp[1]] + 1
            que.append([tmp[0]+1,tmp[1]])
    if tmp[0] > 0:
        if graph[tmp[0]-1][tmp[1]] == 1:
            graph[tmp[0]-1][tmp[1]] = graph[tmp[0]][tmp[1]] + 1
            que.append([tmp[0]-1,tmp[1]])
for i in range(n):
    for j in range(m):
        while(len(que) > 0):
            print(que)
            bfs()
print(graph[n-1][m-1])