# 퇴사 - 45m

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
visited = [False] * n

ans = 0
def dfs(amount, final):

    global ans

    if final > n:
        return

    # final < n 일때 가장 큰 수익을 얻을 경우의 수 때문에 final < n 경우에도 수익을 비교할 필요는 없다.
    # 왜냐하면 final < n일때 가장 큰 수익을 얻었다 해도 그이후에 수업을 하지 않을 경우 정답이 될 수 있기 때문이다.
    if final == n:
        ans = max(amount,ans)
        return

    dfs(amount+a[final][1], final+a[final][0])
    dfs(amount, final+1)

dfs(0,0)

print(ans)