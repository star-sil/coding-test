#가장 긴 증가하는 부분 수열 3
import sys
N = int(input())
numlist = list(map(int,sys.stdin.readline().split()))
for i in range(len(numlist)):
    checklist = []
    check = numlist[i]
    for j in range(i,len(numlist)):
        if(check < numlist[j]):
            checklist.append(numlist[j])
print(len(set(checklist))+1)