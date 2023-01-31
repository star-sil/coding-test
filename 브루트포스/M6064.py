# 카잉 달력
# 시간 초과때문에 건너뛰기 필요
# 마지막 해는 m*n 보다 작을 수 있다.
# 마지막 해 이후 첫번째 해가 정답이 될 수 있으니 주의!!
# 처음 (x,y) 가 이후에 나올 차례는 m*n + 1이 아닌 m*n의 최소공배수 + 1
# => 이게 핵심

t = int(input())

for _ in range(t):
    m, n, nx, ny = map(int,input().split())
    find = False

    if nx == 1 and ny == 1:
        print(1)
        find = True
        continue
    
    x , y = nx - 1, ny - 1

    if nx == 1:
        x = m
    if ny == 1:
        y = n
    
    i = 0
    l = set()
    while True:
        if x + m * i <= m*n:
            l.add(x + m * i)
        
        else:
            break
        i += 1
    
    i = 0

    while True:
        if (y + n * i) in l:
            print(y + n * i+1)
            find = True
            break

        if (y + n * i + 1) > m*n:
            break

        i += 1

    if not find:
        print(-1)
        
        