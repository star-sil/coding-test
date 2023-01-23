# 2x2x2 큐브
# 규칙을 찾아야 한다. 전개도 칸을 기준으로 번호를 매기면
# 회전로직에 따라 항상 같은 칸으로 이동한다는 것을 파악한다.
# x축 y축 z축으로 좌우 회전 총 12개에 대한 이동 로직을 하나 하나 짜야한다.
# 여기서 더 나아가면 왼쪽 방향으로 회전하는 것은 오른쪽 방향으로 3번 회전하는 것과 같다!!

import sys

cube = list(sys.stdin.readline().split())

# z축
def wu(nc, c):
    nc[0] = c[23]
    nc[2] = c[21]
    nc[4] = c[0]
    nc[6] = c[2]
    nc[8] = c[4]
    nc[10] = c[6]
    nc[23] = c[8]
    nc[21] = c[10]
    return verify(nc)

def wd(nc, c):
    nc[0] = c[4]
    nc[2] = c[6]
    nc[4] = c[8]
    nc[6] = c[10]
    nc[8] = c[23]
    nc[10] = c[21]
    nc[23] = c[0]
    nc[21] = c[2]
    return verify(nc)

def hu(nc, c):
    nc[1] = c[22]
    nc[3] = c[20]
    nc[5] = c[1]
    nc[7] = c[3]
    nc[9] = c[5]
    nc[11] = c[7]
    nc[22] = c[9]
    nc[20] = c[11]
    return verify(nc)

def hd(nc, c):
    nc[1] = c[5]
    nc[3] = c[7]
    nc[5] = c[9]
    nc[7] = c[11]
    nc[9] = c[22]
    nc[11] = c[20]
    nc[22] = c[1]
    nc[20] = c[3]
    return verify(nc)

# x축
def rl(nc, c):
    nc[12] = c[20]
    nc[13] = c[21]
    nc[4] = c[12]
    nc[5] = c[13]
    nc[16] = c[4]
    nc[17] = c[5]
    nc[20] = c[16]
    nc[21] = c[17]
    return verify(nc)

def rr(nc, c):
    nc[12] = c[4]
    nc[13] = c[5]
    nc[4] = c[16]
    nc[5] = c[17]
    nc[16] = c[21]
    nc[17] = c[21]
    nc[20] = c[12]
    nc[21] = c[13]
    return verify(nc)

def ll(nc, c):
    nc[14] = c[22]
    nc[15] = c[23]
    nc[6] = c[14]
    nc[7] = c[15]
    nc[18] = c[6]
    nc[19] = c[7]
    nc[22] = c[18]
    nc[23] = c[19]
    return verify(nc)

def lr(nc, c):
    nc[14] = c[6]
    nc[15] = c[7]
    nc[6] = c[18]
    nc[7] = c[19]
    nc[18] = c[22]
    nc[19] = c[23]
    nc[22] = c[14]
    nc[23] = c[15]
    return verify(nc)

# y축
def ul(nc, c):
    nc[20] = c[21]
    nc[21] = c[23]
    nc[22] = c[20]
    nc[23] = c[22]
    nc[0] = c[17]
    nc[1] = c[19]
    nc[12] = c[1]
    nc[14] = c[0]
    nc[10] = c[12]
    nc[11] = c[14]
    nc[17] = c[11]
    nc[19] = c[10]
    return verify(nc)

def ur(nc, c):
    nc[20] = c[22]
    nc[21] = c[20]
    nc[22] = c[23]
    nc[23] = c[21]
    nc[0] = c[14]
    nc[1] = c[12]
    nc[12] = c[10]
    nc[14] = c[11]
    nc[10] = c[19]
    nc[11] = c[17]
    nc[17] = c[0]
    nc[19] = c[1]
    return verify(nc)

def dl(nc, c):
    nc[4] = c[5]
    nc[5] = c[7]
    nc[6] = c[4]
    nc[7] = c[6]
    nc[2] = c[16]
    nc[3] = c[18]
    nc[13] = c[3]
    nc[15] = c[2]
    nc[8] = c[13]
    nc[9] = c[15]
    nc[16] = c[9]
    nc[18] = c[8]
    return verify(nc)

def dr(nc, c):
    nc[4] = c[6]
    nc[5] = c[4]
    nc[6] = c[7]
    nc[7] = c[5]
    nc[2] = c[15]
    nc[3] = c[13]
    nc[13] = c[8]
    nc[15] = c[9]
    nc[8] = c[18]
    nc[9] = c[16]
    nc[16] = c[2]
    nc[18] = c[3]
    return verify(nc)

# 색깔 확인
def verify(c):
    same = True
    for i in range(6):
        for j in range(1,4):
            if c[(j + i*4) - 1] != c[j + i*4]:
                same = False
    return same

ans = 0
if wu(cube[:],cube) or wd(cube[:],cube) or hu(cube[:],cube) or hd(cube[:],cube):
    ans = 1

if rl(cube[:],cube) or rr(cube[:],cube) or ll(cube[:],cube) or lr(cube[:],cube):
    ans = 1

if dl(cube[:],cube) or dr(cube[:],cube) or ul(cube[:],cube) or ur(cube[:],cube):
    ans = 1

print(ans)