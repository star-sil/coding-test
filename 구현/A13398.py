# 연속합 2 - x

n = int(input())
a = list(map(int,input().split()))

d = [0]*n
dr = [0]*n

# i 번째에서 끝나는 최대 연속합 구하기
for i in range(n):
    d[i] = a[i]
    if i == 0:
        continue
    if d[i] < d[i-1] + a[i]:
        d[i] = d[i-1] + a[i]

# i 번째에서 시작하는 최대 연속합 구하기
for i in range(n-1, -1, -1):
    dr[i] = a[i]
    if i == n-1:
        continue
    if dr[i] < dr[i+1] + a[i]:
        dr[i] = dr[i+1] + a[i]

# 수를 제거하지 않았을때 최대 연속합
ans = max(d)

# i 번째 수를 제거했을때 최대 연속합 구하기
for i in range(1, n-1):
    if ans < d[i-1] + dr[i+1]:
        ans = d[i-1] + dr[i+1]
print(ans)
