# 외판원 순회 2 - 30m 22s
# 마지막 마을 -> 첫번째 마을 경로 비용도 고려해야함(만약 0이면 이동 불가)
# 백트래킹 사용가능 -> 시작 마을을 고정해도 된다.

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
visited = [False] * n
ans = float('inf')

def dfs(start, pre, depth, cost):
    global ans

    if depth == n and a[pre][start] != 0:
        ans = min(ans,cost+a[pre][start])

    for i in range(len(a)):
        if visited[i] or a[pre][i] == 0:
            continue
        visited[i] = True
        dfs(start, i,depth+1,cost + a[pre][i])
        visited[i] = False


visited[0] = True
dfs(0, 0, 1, 0)

print(ans)