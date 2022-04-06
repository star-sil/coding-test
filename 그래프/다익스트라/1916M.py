#최소비용 구하기

import sys

N = int(input())  # 그래프 정점 수
M = int(input())

s = 0  # 시작정점
g = [[] for _ in range(M)]

for i in range(M):
    start, des, cost = map(int,input().split())
    g[start-1].append((des-1,cost))

s, d = map(int,input().split())
s -= 1
d -= 1


visited = [False for _ in range(N)]  # 초기화
D = [sys.maxsize for _ in range(N)]  # D[i]를 최댓값으로 초기화
D[s] = 0

for k in range(N):
    m = -1
    min_value = sys.maxsize
    for j in range(N):  # 방문 안된 정점들의 D 원소들 중에서 최솟값을 가진 정점 m 찾기
        if not visited[j] and D[j] < min_value:
            min_value = D[j]
            m = j           
    visited[m] = True
    
    for w, wt in g[m]:  # m에 인접한 방문 안된 각 정점의 D의 원소 갱신
        if not visited[w]:  
            if D[m]+wt < D[w]:             
                D[w] = D[m] + wt  # 간선 완화

print(D[d])