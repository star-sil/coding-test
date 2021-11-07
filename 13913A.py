#숨바꼭질 4
"""
경로 정보와 깊이 정보를 리스트를 이용해서 해당 노드의 값을 
인덱스로 설정해서 해당 인덱스에 경로 정보와 깊이 정보를 입력하는
방식으로 문제를 해결했다. 최단 경로를 구해야 함으로 bfs 알고리즘을 사용했다.
"""
from collections import deque

def path(x):
    arr = []
    temp = x
    for _ in range(dist[x]+1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            path(x)
            return x
        for i in (x+1, x-1, 2*x):
            if 0<=i<=100000 and dist[i]==0:
                q.append(i)
                dist[i] = dist[x] + 1
                move[i] = x

N, K = map(int, input().split())
dist = [0]*100001
move = [0]*100001
bfs()
