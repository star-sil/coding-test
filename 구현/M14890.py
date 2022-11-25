#경사로

'''
칸을 센다 => cnt
다음 칸이 커지는 경우
    1칸 커지는 경우
        경사로 아직 만드는 중 && cnt >= L
            이동 가능
        경사로 만드는 중 아님
            이동 가능
        else
            이동 불가
    else
        이동 불가

다음 칸이 작아지는 경우
    1칸 작아지는 경우
        경사로 아직 만드는 중 && cnt >= L
            이동 가능
        경사로 아직 만드는 중 아님
            이동 가능
        else
            이동 불가
'''

n, l = map(int,input().split())

g = [list(map(int,input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    cnt = 0
    change = False
    pre_block = g[i][0]
    for j in range(n):
        block = g[i][j]
        go = False
        if pre_block == block:
            cnt += 1
            go = True
        elif pre_block > block:
            change = True
            if not change and cnt >= l:
                cnt = 1
                go = True
            elif change and cnt-l >= l:
                cnt = 1
                go = True
        elif pre_block < block:
            change = True
            if not change:
                cnt = 0
                go = True
            elif change and cnt >= l:
                cnt = 0
                go = True
        pre_block = block
        if go and j == n-1:
            ans += 1
        if not go:
            break

for i in range(n):
    cnt = 0
    change = False
    pre_block = g[0][i]
    for j in range(n):
        block = g[j][i]
        go = False
        if pre_block == block:
            cnt += 1
            go = True
        elif pre_block > block:
            change = True
            if not change and cnt >= l:
                cnt = 1
                go = True
            elif change and cnt-l >= l:
                cnt = 1
                go = True
        elif pre_block < block:
            change = True
            if not change:
                cnt = 1
                go = True
            elif change and cnt >= l:
                cnt = 1
                go = True
        pre_block = block
        if go and j == n-1:
            ans += 1
        if not go:
            break

print(ans)
            

        


