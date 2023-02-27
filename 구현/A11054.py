# 가장 긴 바이토닉 부분 수열

n = int(input())
a = list(map(int,input().split()))

d1 = [0]*n
d2 = [0]*n

# i 번째에서 끝나는 가장 긴 증가하는 부분수열의 길이 구하기
for i in range(n):
    d1[i] = 1
    for j in range(i):
        if a[j] < a[i] and d1[j]+1 > d1[i]:
            d1[i] = d1[j]+1

# i 번째에서 시작하는 가장 긴 감소하는 부분 수열의 길이 구하기
for i in range(n-1, -1, -1):
    d2[i] = 1
    for j in range(i+1, n):
        if a[i] > a[j] and d2[j]+1 > d2[i]:
            d2[i] = d2[j]+1

# d1, d2에서 i번째의 값이 중복되므로 -1을 빼준다.
d = [d1[i]+d2[i]-1 for i in range(n)]
print(max(d))
