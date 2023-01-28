# 일곱 난쟁이
# 조합을 이용해 빠르게 푼다.
# sort() 함수 사용시 반환값은 None임을 주의한다.
# => ans = talls.sort() ans는 None!!
# 아홉명 중 일곱명을 고르는 것은 아홉명 중 두명을 고르는 것과 같아.
# => for문으로 두명을 골라 전체 합에서 빼보면서 답을 구하는 방식도 있다.

from itertools import combinations

mini = [int(input()) for _ in range(9)]

mini_talls = list(combinations(mini,7))

ans = []
for talls in mini_talls:
    if sum(talls) == 100:
        talls = list(talls)
        talls.sort()
        ans = talls
        break

for tall in ans:
    print(tall)