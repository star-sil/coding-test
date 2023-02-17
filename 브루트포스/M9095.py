# 1, 2, 3 더하기
# 해답이 항상 깔끔하다는 인식은 버리자
# 시간 복잡도만 충족된다면 해당 문제 처럼 10중 for문으로 해결할 수도 있다.
# 재귀 호출이나 비트마스크를 사용하면 더 간결하게 작성할 수 있다.

t = int(input())

for _ in range(t):
    n = int(input())
    ans = 0
    for a in range(1,4):
        if a == n:
            ans += 1
        for b in range(1,4):
            if a + b == n:
                ans += 1
            for c in range(1,4):
                if a + b + c == n:
                    ans += 1
                for d in range(1,4):
                    if a + b + c + d == n:
                        ans += 1
                    for e in range(1,4):
                        if a + b + c + d + e == n:
                            ans += 1
                        for f in range(1,4):
                            if a + b + c + d + e + f == n:
                                ans += 1
                            for g in range(1,4):
                                if a + b + c + d + e + f + g == n:
                                    ans += 1
                                for h in range(1,4):
                                    if a + b + c + d + e + f + g + h == n:
                                        ans += 1
                                    for i in range(1,4):
                                        if a + b + c + d + e + f + g + h + i == n:
                                            ans += 1
                                        for j in range(1,4):
                                            if a + b + c + d + e + f + g + h + i + j == n:
                                                ans += 1

    print(ans)