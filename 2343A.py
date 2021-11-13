#기타 레슨
'''
불루레이 기준으로 생각하면 된다.
문제가 많다 최대 길이 만큼 배열 나누기, 이진 탐색 둘다 안된다.
'''
import sys
N, M = map(int, sys.stdin.readline().split())
Lecture = list(map(int,sys.stdin.readline().split()))
Max = max(Lecture)
head, tail = Max, sum(Lecture)
result = []
while head <= tail:
    point = (head + tail) // 2
    count = length = 0
    for i in range(len(Lecture)):
        length += Lecture[i]
        if length > point:
            length = Lecture[i]
            count += 1
            continue
        elif length == point:
            length = 0
            count += 1
            continue
    if length > 0:
        count += 1
    if count <= M:
        tail = point - 1
        continue
    elif count > M:
        head = point + 1
        continue
print(tail)