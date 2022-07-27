#연결 요소의 개수

N, M = map(int,input().split())

visited = [ False * i for i in range(N+1)]
g = [[] * i for i in range(N+1)]

for _ in range(M):
    v1, v2 = map(int,input().split())
    g[v1].append(v2)
    g[v2].append(v1)

def dfs(x):
    if visited[x] == False:
        visited[x] = True
        for v in g[x]:
            dfs(v)
count = 0
for i in range(1,N+1):
    if visited[i] == False:
        count += 1
        dfs(i)

print(count)
        


