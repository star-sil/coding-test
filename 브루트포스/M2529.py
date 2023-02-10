# 부등호 - 30m 14s

k = int(input())
a = list(input().split())
ans = []
visited = [False] * 10

# 앞선 부등호 및 숫자, 방문여부, 만든 문자열
def dfs(signIndex, visited, s):

    if len(s) == k+1:
        ans.append(s)
        return

    for i in range(10):
        if visited[i]:
            continue

        if a[signIndex] == '<' and int(s[-1]) < i:
            visited[i] = True
            dfs(signIndex+1, visited, s+str(i))
            visited[i] = False
        elif a[signIndex] == '>' and int(s[-1]) > i:
            visited[i] = True
            dfs(signIndex+1, visited, s+str(i))
            visited[i] = False

for i in range(10):
    visited[i] = True
    dfs(0,visited,str(i))
    visited[i] = False

ans.sort()
print(ans[-1])
print(ans[0])



