# N과 M (4)
# 문제를 잘못 이해했었다.
# => 비 내림차순이라는 뜻은 수열에서 k번째 원소는 k-1 번째 원소보다 크거나 같아야 한다는 것이다.

n, m = map(int,input().split())

nums = []

def dfs(depth,start):
    
    if depth == m:
        print(' '.join(map(str,nums)))
        return
    
    for i in range(start,n+1):
        nums.append(i)
        dfs(depth + 1,i)
        nums.pop()
    
dfs(0,1)

