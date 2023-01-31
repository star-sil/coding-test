# 수 이어 쓰기 1

n = int(input())
a = 10 # 다음 자릿수
b = 1 # 다음 자릿수 개수
ans = 0

while True:

    if a-1 < n:
        ans += (a - a // 10) * b
        a *= 10
        b += 1
        continue
    else:
        ans += (n - a // 10 + 1) * b
        break

print(ans)    