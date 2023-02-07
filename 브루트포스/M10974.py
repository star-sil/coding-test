# 모든 순열
from itertools import permutations

n = int(input())
for perm in permutations(list(range(1,n+1))):
    print(*perm)