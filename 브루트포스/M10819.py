# 차이를 최대로 - 17m 26s
# 순열 사용해도 됨

n = int(input())
a = list(map(int,input().split()))
visited = [False] * n

ans = float('-inf')

def dfs(l):
    global ans

    if len(l) == n:
        value = 0
        for i in range(1,len(l)):
            value += abs(l[i-1] - l[i])
        ans = max(ans, value)

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        l.append(a[i])
        dfs(l)
        visited[i] = False
        l.pop()

dfs([])
print(ans)

