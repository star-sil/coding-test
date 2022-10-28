# DFS 스페셜 저지

N = int(input())
graph = [[] for _ in range(N+1)]
check = [False for _ in range(N+1)]
for _ in range(N-1):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
resultList = list(map(int,input().split()))

dic = {}
for i in range(N):
    dic[resultList[i]] = i
result = []
def dfs(x):
    if check[x]:
        return
    check[x] = True
    result.append(x)

    sortList = []
    for i in graph[x]:
        sortList.append((dic[i],i))
    sortList.sort()

    for i,j in sortList:
        dfs(j)

dfs(1)
ans = 1
for i in range(N):
    if resultList[i] != result[i]:
        ans = 0
print(ans)