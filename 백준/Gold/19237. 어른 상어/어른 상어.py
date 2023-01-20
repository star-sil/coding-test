# 어른 상어

import sys

limit = 1000
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n, m, smell_time = map(int,input().split())

shark = [[0]*n for _ in range(n)]
shark_next = [[0]*n for _ in range(n)]
smell = [[0]*n for _ in range(n)]
smell_who = [[0]*n for _ in range(n)]

dirs = [0] * (m+1)

# 상어별 방향 우선순위
priority = [[[0]*4 for _ in range(4)] for _ in range(m+1)]

# 상어 배치
for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(n):
        shark[i][j] = temp[j]
        # 해당 위치에 상어가 존재하면 냄새 뿌리기
        if shark[i][j] > 0:
            # 냄새 남은 시간
            smell[i][j] = smell_time
            # 누구의 냄새인지
            smell_who[i][j] = shark[i][j]

# 상어 현재 방향
dirs = [0] + [d-1 for d in map(int,input().split())]

# 상어의 수만큼 상어별 방향 우선순위 입력
for i in range(1, m+1):
    for j in range(4):
        priority[i][j] = [d-1 for d in map(int,input().split())]


# 번호 1인 상어만 남았는지 확인
def check_1():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if shark[i][j] > 0:
                cnt += 1
    return cnt == 1


# 상어 이동 함수
def move_shark():
    v = []

    # 상어 찾기
    for i in range(n):
        for j in range(n):
            shark_next[i][j] = 0
            if shark[i][j] > 0:
                # 상어 번호, 행, 열
                v.append((shark[i][j],i,j))
    # 번호가 큰 순으로 상어 정렬                
    v.sort()

    for t in v:
        no, x, y = t
        # 상어의 현재 방향 찾기
        shark_dir = dirs[no]
        # 이동 여부
        ok = False

        # 먼저 방향 우선순위대로 냄새가 없는 곳을 확인
        for k in range(4):
            # 다음 위치 (방향 우선순위 기준)
            nx = x+dx[priority[no][shark_dir][k]]
            ny = y+dy[priority[no][shark_dir][k]]
            if 0 <= nx < n and 0 <= ny < n:
                # 남아있는 냄새가 없는 경우
                if smell[nx][ny] == 0:
                    # 상어가 없는 경우
                    if shark_next[nx][ny] == 0:
                        shark_next[nx][ny] = no
                        dirs[no] = priority[no][shark_dir][k]
                    else: # 상어가 있는 경우
                        if shark_next[nx][ny] > no: # 자신의 번호가 더 작은 경우에만 이동 아니면 제거됨 냄새도 못 뿌린다!!
                            shark_next[nx][ny] = no
                            dirs[no] = priority[no][shark_dir][k]

                    ok = True
                    break

        if not ok: # 이동할 방향에 냄새가 모두 있는 경우 자신의 냄새가 있는 곳으로 이동
            for k in range(4):
                nx = x+dx[priority[no][shark_dir][k]]
                ny = y+dy[priority[no][shark_dir][k]]
                if 0 <= nx < n and 0 <= ny < n:
                    # 냄새가 있고 냄새 흔적이 자신인 경우에만 이동
                    if smell_who[nx][ny] == no:
                        shark_next[nx][ny] = no
                        dirs[no] = priority[no][shark_dir][k]
                        break

    for i in range(n):
        for j in range(n):
            shark[i][j] = shark_next[i][j]
            if smell[i][j] > 0:
                smell[i][j] -= 1
            if smell[i][j] == 0:
                smell_who[i][j] = 0
            if shark[i][j] > 0:
                smell[i][j] = smell_time
                smell_who[i][j] = shark[i][j]




ans = -1

for t in range(1, limit+1):
    move_shark()
    if check_1():
        ans = t
        break
print(ans)