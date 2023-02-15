# 리모컨
# m == 0 일경우 주의...
# 범위 1000000 해야하는 이유
# 숫자 버튼을 누루고 +,- 버튼을 눌러야하는 부분에서 오랜시간 소요
# 바로 알고리즘 해결을 고민하는 것이 아닌 문제해결 방안을 생각해보고 적용할 수 있는 알고리즘을 고민한다.

from collections import deque

f = 800000

channel = [-1] * (f+1)

n = int(input())
m = int(input())
broke = set()

if m > 0:
    broke = set(map(int,input().split()))

dq = deque()

for i in range(10):
    if i in broke:
        continue

    dq.append(i)
    channel[i] = 1

while dq:
    x = dq.popleft()
    for i in range(10):
        if i in broke:
            continue
        
        nx = x * 10 + i

        if 0 <= nx <= f and channel[nx] == -1:
            channel[nx] = channel[x] + 1
            dq.append(nx)

ans = 500000

for i in range(f+1):
    if channel[i] != -1:
        ans = min(ans,abs(n - i)+channel[i])

if abs(n - 100) < ans:
    ans = abs(n-100)

print(ans)







