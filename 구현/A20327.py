# 배열 돌리기 6
# 부분 배열 구하기
# 부분 배열을 만들때는 시작 칸을 정하고 일정한 길이로 부분 배열의 범위를 설정한다.

n,r = map(int,input().split())
size = (1 << n)
g = [list(map(int,input().split())) for _ in range(2**n)]


def mirror_UD(g): # 1 상하반전
    return [g[i][:] for i in range(len(g)-1,-1,-1)]

def mirror_LR(g): # 2 좌우반전
    return [g[i][::-1] for i in range(len(g))]

def rotate_R(g): # 3 오른쪽 90도 회전
    ans = []
    for i in range(len(g[0])):
        ans.append([g[j][i] for j in range(len(g)-1,-1,-1)])
    return ans

def rotate_L(g): # 4 왼쪽 90도 회전
    ans = []
    for i in range(len(g[0])-1,-1,-1):
        ans.append([g[j][i] for j in range(len(g))])
    return ans

def operation5(a, l):
    n = len(a)
    ans = [[0]*n for _ in range(n)]
    sub_size = (1 << l)
    sub_count = n // sub_size
    for i in range(sub_count):
        for j in range(sub_count):
            x1 = i*sub_size
            y1 = j*sub_size
            x2 = (sub_count-i-1)*sub_size
            y2 = j*sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1+x][y1+y] = a[x2+x][y2+y]
    return ans

def operation6(a, l):
    n = len(a)
    ans = [[0]*n for _ in range(n)]
    sub_size = (1 << l)
    sub_count = n // sub_size
    for i in range(sub_count):
        for j in range(sub_count):
            x1 = i*sub_size
            y1 = j*sub_size
            x2 = i*sub_size
            y2 = (sub_count-j-1)*sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1+x][y1+y] = a[x2+x][y2+y]
    return ans

def operation7(a, l):
    n = len(a)
    ans = [[0]*n for _ in range(n)]
    sub_size = (1 << l)
    sub_count = n // sub_size
    for i in range(sub_count):
        for j in range(sub_count):
            x1 = i*sub_size
            y1 = j*sub_size
            x2 = (sub_count-j-1)*sub_size
            y2 = i*sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1+x][y1+y] = a[x2+x][y2+y]
    return ans

def operation8(a, l):
    n = len(a)
    ans = [[0]*n for _ in range(n)]
    sub_size = (1 << l)
    sub_count = n // sub_size
    for i in range(sub_count):
        for j in range(sub_count):
            x1 = i*sub_size
            y1 = j*sub_size
            x2 = j*sub_size
            y2 = (sub_count-i-1)*sub_size
            for x in range(sub_size):
                for y in range(sub_size):
                    ans[x1+x][y1+y] = a[x2+x][y2+y]
    return ans


def operation_1_to_4(a, k, sx, sy, length):
    b = [[0]*length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            b[i][j] = a[sx+i][sy+j]

    if k == 1:
        b = mirror_UD(b)
    elif k == 2:
        b = mirror_LR(b)
    elif k == 3:
        b = rotate_R(b)
    elif k == 4:
        b = rotate_L(b)

    for i in range(length):
        for j in range(length):
            a[sx+i][sy+j] = b[i][j]

for _ in range(r):
    k, l = map(int, input().split())
    sub_size = (1 << l)
    if 1 <= k <= 4:
        for i in range(0, size, sub_size):
            for j in range(0, size, sub_size):
                operation_1_to_4(g, k, i, j, sub_size)
    elif 5 <= k <= 8:
        if k == 5:
            g = operation5(g, l)
        elif k == 6:
            g = operation6(g, l)
        elif k == 7:
            g = operation7(g, l)
        elif k == 8:
            g = operation8(g, l)

for i in range(size):
    print(' '.join(map(str,g[i])))
