# N과 M(2)

from itertools import permutations

n, m = map(int,input().split())

for combin in permutations(list(range(1,n+1)),m):
    print(*combin)
