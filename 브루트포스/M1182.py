# 부분수열의 합
# 부분 수열의 특징 제대로 숙지!! 공집합은 수열이 아님 -> 필기자료 확인하기

n, m = map(int,input().split())
a = list(map(int,input().split()))

ans = 0
def dfs(index, s, size):

    global ans

    if index == n:
        if s == m and size > 0:
            ans += 1
        return

    dfs(index+1,s+a[index],size+1)
    dfs(index+1,s,size)

dfs(0,0,0)

print(ans)