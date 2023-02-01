# N과 M (7)

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []


def dfs(depth):

    if depth == m:
        print(' '.join(map(str, ans)))
        return

    for i in nums:
        ans.append(i)
        dfs(depth+1)
        ans.pop()

dfs(0)