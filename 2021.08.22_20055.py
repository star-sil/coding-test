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

# from collections import deque
# import sys

# input = sys.stdin.readline
# n,k = map(int,input().split())
# A = deque(map(int,input().split()))
# ans =1

# #robot이 들어온 순서대로 현재 자신의 위치를 담고있는다
# robot =deque([0]*(n*2))

# while(True):
#     #1
#     A.rotate(1)
#     robot.rotate(1)
#     robot[n-1]=0 #내려가는 위치에 로봇 삭제

#     #2
#     for i in range(n-2,-1,-1):
#         if(robot[i]!=0 and robot[i+1]==0 and A[i+1]>=1):
#             A[i+1]-=1
#             robot[i+1]=robot[i]
#             robot[i]=0
#     robot[n-1]=0

#     #3
#     if(robot[0]==0 and A[0]>0):
#         A[0]-=1
#         robot[0]=1

#     #4
#     cnt=0
#     for i in range(len(A)):
#         if(A[i]==0):
#             cnt+=1

#     if(cnt>=k):
#         print(ans)
#         break

#     ans+=1


         

        

