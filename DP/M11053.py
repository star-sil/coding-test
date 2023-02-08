# 가장 긴 증가하는 부분 수열
# max(list) => 가장 큰 원소 반
# 수열을 문자로 입력 받아서 정답이 계속 틀렸다...

n = int(input())
a = list(map(int,input().split()))
d = [0] * n

for i in range(n):
    d[i] = 1
    for j in range(i-1,-1,-1):
        if a[i] > a[j] and d[i] < d[j] + 1:
            d[i] = d[j] + 1

print(max(d))