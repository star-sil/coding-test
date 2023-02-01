# N과 M(3)

n, m = map(int,input().split())

nums = []

def dfs(depth):
    
    if depth == m:
        print(' '.join(map(str,nums)))
        return
    
    for i in range(1,n+1):
        nums.append(i)
        dfs(depth + 1)
        nums.pop()
    
dfs(0)

