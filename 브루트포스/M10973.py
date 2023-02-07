# 이전 순열
import sys
n = int(input())
nums = list(map(int,sys.stdin.readline().split()))

def next_permutation(l, n):
    i = n-1
    for i in range(n-1,-1,-1):
        if i == 0:
            return False
        if l[i] < l[i-1]:
            i -= 1
            break

    j = n-1
    for j in range(n-1,-1,-1):
        if l[j] < l[i]:
            break

    l[i], l[j] = l[j], l[i]

    tmp = l[i+1:]
    tmp.reverse()
    l = l[:i+1] + tmp

    for k in l:
        print(k, end=" ")

    return True

if not next_permutation(nums, n):
    print(-1)
