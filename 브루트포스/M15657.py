# N과 M (8)

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []


def dfs(depth, start):

    if depth == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(start, len(nums)):
        ans.append(nums[i])
        dfs(depth+1, i)
        ans.pop()

dfs(0, 0)