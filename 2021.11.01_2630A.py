#색종이 만들기
import sys
n = int(input())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
White, Blue = 0, 0

def Distinguish(x, y, N):
    global White, Blue
    tmp = 0
    for i in range(x, x + N):
        for j in range(y, y + N):
            #행렬이 1일 경우(파란색)
            if B[i][j]:
                tmp += 1
    #모든 행이 0일경울(하얀색)
    if not tmp:
        White += 1
    #모든 행렬이 1일 경우(파란색)
    elif tmp == N**2:
        Blue += 1
    #행령에 0과 1이 섞여있는 경우 4등분 한다.
    else:
        Distinguish(x, y, N // 2)
        Distinguish(x + N // 2, y, N // 2)
        Distinguish(x, y + N // 2, N // 2)
        Distinguish(x + N // 2, y + N // 2, N // 2)
    return

Distinguish(0, 0, n)
print(White)
print(Blue)