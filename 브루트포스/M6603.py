# 로또 - 12m 7s
from itertools import combinations

while True:
    a = list(map(int,input().split()))
    k = a[0]
    if k == 0:
        break
    a = a[1:]

    for com in combinations(a,6):
        print(*com)
    print()
