#돌 그룹
# 총 합은 변하지 않는다.
# 노드를 x,y,z로 나타내면 메모리를 초과한다.
# 따라서 x,y로만 노드를 나타내고 나머지 z는 총합에서 나머지를 구하는 연산을 사용해 구한다.
import sys
from collections import deque
A, B, C = map(int, input().split())
s = A + B + C
visit = [[False] * 1001 for _ in range(1001) ]

def cal(x,y):
    if x > y:
        x = x - y
        y = 2 * y
    else:
        y = y - x
        x = 2 * x
    return x, y


if s % 3 != 0:
    print(0)
    sys.exit()

ans = 0
dq = deque()
dq.append((A,B))
visit[A][B] = True
while dq:
    x, y = dq.popleft()
    z = s - x - y
    if x == y and y == z:
        ans = 1
        break
    if x != y:
        a,b = cal(x,y)
        if a <= 1000 and b <= 1000 and visit[a][b] == False:
            visit[a][b] = True
            dq.append((a,b))
        
    if x != z:
        a,b = cal(x,z)
        if a <= 1000 and b <= 1000 and visit[a][y] == False:
            visit[a][y] = True
            dq.append((a,y))
        
    if y != z:
        a,b = cal(y,z)
        if a <= 1000 and b <= 1000 and visit[x][a] == False:
            visit[x][a] = True
            dq.append((x,a))

print(ans)
