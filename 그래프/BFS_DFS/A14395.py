# 4 연산
# 범위가 10억이여서 실제 노드의 개수를 계산해보면 최대 900개가 되므로 BFS 연산이 가능하다
# 따라서 범위가 너무 많다고 하더라도 최적화를 통해 노드의 개수를 줄여보자

import sys
from collections import deque

MAX = 10 ** 9
check = set()

s, t = map(int,input().split())
if s == t:
    print(0)
    sys.exit()

dq = deque()
dq.append((s,''))
check.add(s)
while dq:
    x, st = dq.popleft()
    if x == t:
        if s == t:
            print(0)
        else:
            print(st)
        sys.exit()
    if 0 <= x * x < MAX + 1 and x * x not in check:
        dq.append((x*x,st+'*'))
        check.add(x*x)
    if 0 <= x + x < MAX + 1 and x + x not in check:
        dq.append((x+x,st+'+'))
        check.add(x+x)
    if 0 <= x - x < MAX + 1 and x - x not in check:
        dq.append((x-x,st+'-'))
        check.add(x-x)
    if x > 0 and 0 <= x // x < MAX + 1 and x // x not in check:
        dq.append((x/x,st+'/'))
        check.add(x*x)
print(-1)