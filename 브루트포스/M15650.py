# N과 M(2)
# 조합 문제

from itertools import combinations

n, m = map(int,input().split())

for combin in combinations(list(range(1,n+1)),m):
    print(*combin)