# 종이 조각

n, m = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]
ans = 0

for s in range(1<<(n*m)): # 비트마스크를 만든다 -> 2^(n*m)
    # 0은 가로, 1은 세기로
    sum = 0
    # 가로 부분 구하기
    for i in range(n):
        cur = 0
        for j in range(m):
            k = i*m+j
            if (s&(1<<k)) == 0: # 가로가 시작되거 연속된다.
                cur = cur * 10 + a[i][j]
            else: # 세로인 경우 지금까지 만든수를 더하고 0으로 만든다.
                sum += cur
                cur = 0
        # 마지막 부분을 더하지 않고 끝날 수 있다. -> 마지막 부분이 가로인 경우
        # 마지막 부분이 세로인 경우 cur이 0이므로 0을 더해도 상관없다.
        sum += cur

    # 세로부분 구하기
    for j in range(m):
        cur = 0
        for i in range(n):
            k = i*m+j
            if (s&(1<<k)) != 0:
                cur = cur * 10 + a[i][j]
            else:
                sum += cur
                cur = 0
        sum += cur
    ans = max(ans, sum)
print(ans)




