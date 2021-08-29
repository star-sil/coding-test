import sys
N, K = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
A_ = list()
for i in range(len(A)):
    if i == 0:
        A_.append([A[i],0,'u'])
    elif i == N-1:
        A_.append([A[i],0,'d'])
    else:    
        A_.append([A[i],0,'n'])
A = A_
#회전 시키기
u_pos = d_pos = 0
def lotation(a):
    #위치 탐색
    global u_pos, d_pos
    for i in range(len(a)):
        if a[i][2] == 'u':
            a[i][2] = 'n'
            u_pos = i-1
        elif a[i][2] == 'd':
            a[i][2] = 'n'
            d_pos = i-1
        else:
            continue
    a[u_pos][2] = 'u'
    a[d_pos][2] = 'd'
    if a[d_pos][1] == 1:
        a[d_pos][1] = 0
    return a
#로봇 이동시키기
def move(a):
    for i in range(N*2-1,-1,-1):
        if a[i][1] == 1:
            pos = i
            n_pos = (i+1) % (2*N)
            if a[n_pos][0] != 0 and a[n_pos][1] != 1:
                #발판이 내리는 곳일 경우 아닌경우
                if a[n_pos][2] == 'd':
                    a[pos][1] = 0
                    a[n_pos][0] -= 1
                    a[n_pos][1] = 0
                else:
                    a[pos][1] = 0
                    a[n_pos][0] -= 1
                    a[n_pos][1] = 1
    return a

def count_zero(a):
    count = 0
    for i in a:
        if i[0] == 0:
            count += 1
    return count


count = 0
while True:
    count += 1
    A = lotation(A)
    A = move(A)
    if A[u_pos][0] != 0:
        A[u_pos][0] -= 1
        A[u_pos][1] = 1

    if count_zero(A) >= K:
        break
print(count)

         

        

