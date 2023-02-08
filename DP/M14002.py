# 가장 긴 증가하는 부분 수열 4

n = int(input())
a = list(map(int,input().split()))
d = [0] * n
v = [0] * n

for i in range(n):
    d[i] = 1
    for j in range(i):
        if a[j] < a[i] and d[j]+1 > d[i]:
            d[i] = d[j]+1
            v[i] = j

m = max(d)
index = 0
for i in range(len(d)):
    if m == d[i]:
        index = i
        break

ans = []
while True:
    ans.append(a[index])

    if d[index] == 1:
        break

    index = v[index]

ans.reverse()
print(*ans)

