#가장 긴 증가하는 부분 수열 3
"""
시간 초과하는 부분을 어떻게 풀어야 할지를 알았지만
그래도 시간 복잡도를 줄이지 못했다. 어디서 문제인지 탐색부분을
다시 확인해봐야 겠다. 시간 복잡도는 nlog(n)이어야 한다."""
import sys
from collections import deque
N = int(input())
numlist = deque(map(int,sys.stdin.readline().split()))
def lower_bound(left,numlist):
    head, tail = 0, len(numlist)-1
    while head <= tail:
        mid = (head+tail) // 2
        if numlist[mid] > left:
            tail = mid - 1
        else:
            head = mid + 1
    return tail

result = 0
for _ in range(N):
    left =numlist.popleft()
    sort = sorted(set(numlist))
    index = lower_bound(left+1,sort)
    count = len(sort) - index
    if result < count:
        result = count
print(result)