# 배열 돌리기2

n,m,r = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
groups = []
groupn = min(n,m) // 2

for k in range(groupn):
    group = []
    for j in range(k,m-k):
        group.append(a[k][j])
    for i in range(k+1,n-k-1):
        group.append(a[i][m-k-1])
    for j in range(m-k-1,k,-1):
        group.append(a[n-k-1][j])
    for i in range(n-k-1,k,-1):
        group.append(a[i][k])
    groups.append(group)

for k in range(groupn):
    group = groups[k]
    l = len(group)
    index = r%l
    for j in range(k, m-k):
        a[k][j] = group[index]
        index = (index+1)%l
    for i in range(k+1, n-k-1):
        a[i][m-k-1] = group[index]
        index = (index+1)%l
    for j in range(m-k-1,k,-1):
        a[n-k-1][j] = group[index]
        index = (index+1)%l
    for i in range(n-k-1,k,-1):
        a[i][k] = group[index]
        index = (index+1)%l

for row in a:
    print(' '.join(map(str,row)))