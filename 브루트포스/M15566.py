# N과 M(6)

n,m = map(int,input().split())

nums = list(map(int,input().split()))
nums.sort()
visited = [False] * (nums[-1]+1)

ans = []

def dfs(depth,start):

    if depth == m:
        print(' '.join(map(str,ans)))
        return
    
    for i in range(start,len(nums)):
        if not visited[nums[i]]:
            ans.append(nums[i])
            visited[nums[i]] = True
            dfs(depth+1,i+1)
            visited[nums[i]] = False
            ans.pop()

dfs(0,0)