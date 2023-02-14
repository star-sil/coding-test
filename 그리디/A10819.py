# 차이를 최대로
# 그리디로 풀면 고려해야할것이 많다.
# 일단 기본으로 생각한 로직은 1번째 큰수, 1번째 작은수, 2번째 큰수....이런 순서로 배열한다음
# 맨 뒤에있는 수를 맨앞으로 옮기는 로직을 생각했다.
# 하지만 이 로직에서 맨앞으로 안옮기는 경우가 더 큰 경우가 있으므로 ex) 3 3 1 둘다 비교해야한다.

n = int(input())
a = list(map(int,input().split()))
a.sort()
d = a[::-1]

b = []
for i in range(len(a)//2):
    b.append(d[i])
    b.append(a[i])

if len(a) % 2 != 0:
    b.append(a[n//2])


ans1 = 0
for i in range(1, len(b)):
    ans1 += abs(b[i - 1] - b[i])

c = b[n-1:] + b[:n-1]

ans2 = 0
for i in range(1, len(c)):
    ans2 += abs(c[i - 1] - c[i])
print(ans2)