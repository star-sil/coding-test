# 단지번호 붙이기
import sys
sys.setrecursionlimit(10**7)
N = int(input())

visited = [[] for i in range(N)]

for i in range(N):
    str = sys.stdin.readline()
    for word in str:
        if word == "0":
            visited[i].append(0)
        else:
            visited[i].append(1)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x, y,count):
    if x >= 0 and y >= 0 and x < N and y < N and visited[x][y] == 1:
        visited[x][y] = 0
        count += 1
        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            count = max(count,dfs(x1,y1,count))
    else:
        return count
    return count

result = 0
result2 = []
for i in range(N):
    for j in range(N):
        if(visited[i][j] == 1):
            count = 0
            result += 1
            result2.append(dfs(i,j,count))

print(result)
result2.sort()
for i in result2:
    print(i)