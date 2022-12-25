# 이차원 배열과 연산
# 해당 문제는 A[r-1][c-1]에 들어있는 값이 K가 되는 최소 시간을 구하는 것이다.
# 여기서 이슈는 배열 A의 열과 행의 크기는 변하기 때문에 목표로하는 r, c의 길이 보다
# 작을 수 있어 해당 값보다 같거나 클경우에 값을 확인하는 과정을 거쳐야했다.
# 난 여기서 클경우에만 확인하고 같은 경우에는 확인하지 않아 오랜시간 틀리게 되었다.
# 같은 경우를 확인해야 하는 경우는 A[r-1][c-1]의 값을 확인하는 것이기 때문에
# 최대 행, 열의 길이가 r, c이면 열과 행의 최대 가능한 인덱스는 r-1, c-1 이므로
# 최대 행, 열의 길이는 목표로 하는 r, c와 같거나 커야 값을 확인할 수 있다.

def calR(a):

    b = []
    for i in range(len(a)):
        tmp = []
        g = [0] * 100
        for j in range(len(a[0])):
            if a[i][j] > 0:
                g[a[i][j]-1] += 1
        # 갯수 맵핑
        for j in range(100):
            if g[j] > 0:
                tmp.append((g[j],j+1)) # 등장 횟수, 수
        b.append(tmp)
        
    # 정렬
    for i in b:
        i.sort()
    
    # 다시 배열 생성
    new_a = []
    length = 0
    for i in range(len(b)):
        length = max(length,len(b[i])*2)
        tmp = []
        for j in range(len(b[i])): # 행마다 길이가 다르다.
            tmp.append(b[i][j][1])
            tmp.append(b[i][j][0])
        new_a.append(tmp)
    
    if length > 100:
        length = 100

    # 배열이 100 이상이면 자르고 최대 길이보다 작으면 0으로 채움
    for i in range(len(new_a)):
        if len(new_a[i]) > 100:
            new_a[i] = new_a[i][:100]
        if len(new_a[i]) < length:
            l = length-len(new_a[i])
            for j in range(l):
                new_a[i].append(0)
    
    return new_a

def calC(a):
    b = []

    for i in range(len(a[0])):
        tmp = []
        g = [0] * 100
        for j in range(len(a)):
            if a[j][i] > 0:
                g[a[j][i]-1] += 1
        # 갯수 맵핑
        for j in range(100):
            if g[j] > 0:
                tmp.append((g[j],j+1)) # 등장 횟수, 수
        b.append(tmp)

    # 정렬
    for i in b:
        i.sort()

    # 길이 구하기
    length = 0
    for i in range(len(b)):
        length = max(length,len(b[i]))
    
    if length > 50:
        length = 50

    for i in range(len(b)):
        if len(b[i]) < length:
            l = length - len(b[i])
            for j in range(l):
                b[i].append((0,0))
        elif len(b[i]) > 50:
            b[i] = b[i][:50]
        
    
    
    # 다시 배열 생성
    new_a = []

    for _ in range(length*2):
        new_a.append([])
    
    
    for i in range(len(b)):
        l = len(b[i])
        for j in range(l): # 행마다 길이가 다르다.
            new_a[2*j].append(b[i][j][1])
            new_a[2*j+1].append(b[i][j][0])
    
    return new_a

    

r,c,k = map(int,input().split())



a = [list(map(int,input().split())) for _ in range(3)]


cnt = 0

for _ in range(100):

    if len(a) >= r and len(a[0]) >= c and a[r-1][c-1] == k:
        print(cnt)
        exit()
    
    cnt += 1 

    # 갯수 구하기 R 연산
    if len(a) >= len(a[0]):
        a = calR(a)
    else:
        a = calC(a)

print(-1)