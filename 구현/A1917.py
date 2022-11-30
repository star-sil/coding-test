# 정육면체 전개도
# 정육면체 전개도 유형은 총 11개 존재
# 11개의 유형은 다 방면으로 대칭(2) 90도 회전(4)의 모양으로 변환 가능
# 따라서 11개의 유형을 미리 지정한다음 회전과 대칭을 통해 전개도인지 아닌지 유뮤를 판별
# 1차원 배열 좌우 대칭, 90도 회전 로직 암기

cubes = [
    ["0010",
     "1111",
     "0010"],
    ["0100",
     "1111",
     "1000"],
    ["0010",
     "1111",
     "0100"],
    ["0001",
     "1111",
     "1000"],
    ["0001",
     "1111",
     "0100"],
    ["11100",
     "00111"],
    ["1100",
     "0111",
     "0010"],
    ["1100",
     "0111",
     "0001"],
    ["0010",
     "1110",
     "0011"],
    ["0001",
     "1111",
     "0001"],
    ["1100",
     "0110",
     "0011"]
]

def mirror(b): # 좌우 대칭 함수
    ans = []
    for i in range(len(b)):
        temp = b[i][::-1] # 1차원 배열 좌우 대칭
        ans.append(temp)
    return ans

def rotate(b): # 90도 회전 함수 시계방향
    ans = [''] * len(b[0])
    for j in range(len(b[0])):
        for i in range(len(b)-1, -1, -1):
            ans[j] += b[i][j]
    return ans

'''
1 2 3 4
5 6 7 8

5 1
6 2
7 3
8 4
'''

def check(a, b, x, y):
    n = len(a)
    for i in range(len(b)):
        for j in range(len(b[0])):
                nx = x+i
                ny = y+j
                if 0 <= nx < n and 0 <= ny < n:
                    if b[i][j] == '0':
                        if a[nx][ny] == 1:
                            return False
                    elif  b[i][j] == '1':
                        if a[nx][ny] == 0:
                            return False
                else:
                    return False
    return True

t = 3
for _ in range(t):
    n = 6
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    ans = False
    for c in cubes:
        cube = [row[:] for row in c]
        for mir in range(2): # 대칭 1번
            for rot in range(4): # 90도 회전 3번 4번은 원상태이니깐
                for i in range(n):
                    for j in range(n):
                        ans |= check(a, cube, i, j)
                cube = rotate(cube)
            cube = mirror(cube)
    print("yes" if ans else "no")