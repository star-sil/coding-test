#신업 사원
import sys

def Count(li):
    sortList = sorted(li)
    min = sortList[0][1]
    count = 0
    for i in range(1,len(sortList)):
        if min > sortList[i][1]:
            min = sortList[i][1]
            count += 1
    return count

T = int(sys.stdin.readline())
tList = []
for _ in range(T):
    N = int(input())
    tmp = [list(map(int,input().split())) for _ in range(N)]
    tList.append(tmp)
   
for li in tList:
        print(Count(li)+1)