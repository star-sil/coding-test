#배열 돌리기3

n,m,r = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
b = list(map(int,input().split()))

def make_graph(v,a,n,m):
    if v == 2:
        for i in range(n):
            for j in range(m//2):
                tmp = a[i][j]
                a[i][j] = a[i][(m-1)-j]
                a[i][(m-1)-j] = tmp
        return a,n,m
    elif v == 1:
        for i in range(n//2):
            for j in range(m):
                tmp = a[i][j]
                a[i][j] = a[(n-1)-i][j]
                a[(n-1)-i][j] = tmp
        return a,n,m
    elif v == 3:
        c = [[0] * (n) for _ in range(m)]
        for i in range(n):
            for j in range(m):
                c[j][(n-1) - i] = a[i][j]
        tmp = n
        n = m
        m = tmp
        return c,n,m
    
    elif v == 4:
        c = [[0] * (n) for _ in range(m)]
        for i in range(n):
            for j in range(m):
                c[(m-1) - j][i] = a[i][j]
        tmp = n
        n = m
        m = tmp
        return c,n,m
    
    elif v == 5:
        c = [[0] * (m) for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i < n//2 and j < m//2:
                    c[i][m//2 + j] = a[i][j]
                elif i < n//2 and j >= m//2:
                    c[n//2 + i][j] = a[i][j]
                elif i >= n//2 and j >= m//2:
                    c[i][j-m//2] = a[i][j]
                elif i >= n//2 and j < m //2:
                    c[i-n//2][j] = a[i][j]
        return c,n,m
    
    elif v == 6:
        c = [[0] * (m) for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i < n//2 and j < m//2: #1
                    c[i+n//2][j] = a[i][j]
                elif i < n//2 and j >= m//2: #2
                    c[i][j-m//2] = a[i][j]
                elif i >= n//2 and j >= m//2: #3
                    c[i-n//2][j] = a[i][j]
                elif i >= n//2 and j < m //2: #4
                    c[i][j+m//2] = a[i][j]
        return c,n,m

for i in b:
    a,n,m = make_graph(i,a,n,m)

for i in range(n):
    for j in range(m):
        print(a[i][j],end=' ')
    print()