# 컨베이어 벨트 위의 로봇
from collections import deque

n, k = map(int, input().split())

belts = list(map(int,input().split()))
robots = [False] * n

ans = 0
while True:
    
    ans += 1

    # 벨트 & 로봇 회전
    tmp = [0] * 2 * n
    for i in range(2*n):
        tmp[(i+1) % (2*n)] = belts[i]
    belts = tmp

    tmp = [0] * len(robots)
    for i in range(len(robots)):
        tmp[(i+1) % len(robots)] = robots[i]
    robots = tmp

    # 내리는 위치에 있는 로봇 제거
    if robots[n-1]:
        robots[n-1] = False
    
    # 로봇 이동 가장 먼저 올라간 로봇부터 이동
    for i in range(len(robots)-2,-1,-1):
        if robots[i] and not robots[i+1] and belts[i+1] > 0:
            robots[i+1] = True
            robots[i] = False
            belts[i+1] -= 1

            if i+1 == n-1:
                robots[i+1] = False
    
    # 로봇 올리기
    if not robots[0] and belts[0] > 0:
        belts[0] -= 1
        robots[0] = True
    
    cnt = 0
    for belt in belts:
        if belt == 0:
            cnt += 1
        if cnt >= k:
            print(ans)
            exit()
    