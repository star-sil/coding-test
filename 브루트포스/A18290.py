# NM과 K (1)

n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ans = float('-inf')

def dfs(depth, value):
    global ans

    if depth == k:
        ans = max(ans, value)
        return

    for i in range(n):
        for j in range(m):

            if visit[i][j]:
                continue

            go = True
            for l in range(4):
                nx, ny = i + dx[l], j + dy[l]

                if 0 <= nx < n and 0 <= ny < m and visit[nx][ny]:
                    go = False
                    break

            if go:
                visit[i][j] = True
                dfs(depth + 1, value + a[i][j])
                visit[i][j] = False

dfs(0, 0)

print(ans)