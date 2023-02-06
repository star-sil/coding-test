# 부분수열의 합2
# 문제 이해를 잘못했다...
# 정수가 주어지면 정수를 뽑 부분수열을 만드는 것이다.
# 1, 2, 3, 4 + s:4 => 1,3 과 4

n, s = map(int,input().split())
a = list(map(int,input().split()))
b1 = a[:n//2]
b2 = a[n//2:]

def dfs(start, value, l, b):

    for i in range(start,len(b)):
        l.append(value)
        dfs(i+1,value+b[i],l,b)

    return l

c1 = dfs(0,0,[],b1)
c2 = dfs(0,0,[],b2)

c1.sort()
c2.sort(reverse=True)

ans = 0
i, j = 0, 0
while True:

    if i >= len(c1) or j >= len(c2):
        break

    if c1[i] + c2[j] == s:
        i += 1
        j += 1
        f = 1
        e = 1
        # 앞으로 이동해도 같은 원소일 경우 예외 처리
        while i < len(c1) and c1[i] == c1[i-1]:
            f += 1
            i += 1
        while j < len(c2) and c2[j] == c2[j-1]:
            e += 1
            j += 1

        ans += f * e

    elif c1[i] + c2[j] < s:
        i += 1

    elif c1[i] + c2[j] > s:
        j += 1

print(ans if s != 0 else ans - 1)
