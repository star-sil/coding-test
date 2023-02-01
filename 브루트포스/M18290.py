# NM과 K (1)
# N중 for문으로 돌릴시 너무 복잡해짐
# 재귀로 해야함
# 경우의 수가 넘어가서 백트래킹 필요

from copy import deepcopy

n, m, k = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ans = 0


def dfs(depth, value, visited):
    global ans

    if depth == k:
        ans = max(ans, value)
        return

    # 더 탐색할 필요가 있는지 확인
    go = False
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and ans <= value + a[i][j]:
                go = True

    if not go:
        return

    for i in range(n):
        for j in range(m):

            if not visited[i][j]:
                visited[i][j] = True
                value += a[i][j]

                nvisited = deepcopy(visited)

                for l in range(4):
                    nx, ny = i + dx[l], j + dy[l]

                    if 0 <= nx < n and 0 <= ny < m:
                        nvisited[nx][ny] = True

                dfs(depth + 1, value, nvisited)

                value -= a[i][j]
                visited[i][j] = False


dfs(0, 0, visit)

print(ans)
