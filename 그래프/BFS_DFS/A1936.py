#소수 경로
#에라토스의 체라는 소수의 여부를 알아내는 것이 필요했다.
#또한 탐색 문제에서는 간선, 정점이 무엇인지 간선의 가중치가 무엇인지 아는것이 중요하다.
from collections import deque

T = int(input())
n = 10000
chain = [True] * n
m = int(n ** 0.5)
for i in range(2,m+1):
    if chain[i] == True:
        for j in range(i+i,n,i):
            chain[j] = False

dx = [i for i in range(10)]


for _ in range(T):
    s, e = input().split()
    dq = deque()
    dq.append(s)
    visit = [-1] * 10000
    visit[int(s)] = 0
    
    while dq:
        x = dq.popleft()
        for index in range(4):
            for num in range(10):
                if index == 0 and num == 0:
                    continue
                if x[index] == str(num):
                    continue
                dx = list(x)
                dx[index] = str(num)
                dx = ''.join(dx)
                if chain[int(dx)] and visit[int(dx)] == -1:
                    visit[int(dx)] = visit[int(x)] + 1
                    dq.append(dx)

    print(visit[int(e)])