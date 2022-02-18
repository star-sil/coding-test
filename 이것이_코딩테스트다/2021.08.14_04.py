map_size = list(map(int,input().split()))
position = list(map(int,input().split()))
map_ = []
count = count2 = 0
for i in range(map_size[0]):
    tmp = list(map(int,input().split()))
    map_.append([i for i in tmp])

def decision(row,col,n,m):
    row += n
    col += m
    if row < 1 or row > map_size[0]:
        return 0
    elif col < 1 or col > map_size[1]:
        return 0
    elif map_[row][col] == 1:
        return 0
    elif map_[row][col] == 0:
        return 1
    elif map_[row][col] == 2:
        return 2
    else:
        print('error')
map_[position[0]][position[1]] = 2
while(1):
    if position[2] == 0:
        if decision(position[0],position[1],0,-1) != 1:
            if count2 != 4:
                count2 += 1
                position[2] = 3
                continue
            if decision(position[0],position[1],1,0) == 0:
                break
            elif decision(position[0],position[1],1,0) == 1:
                count2 = 0
                position[0] += 1
                count += 1
                continue
            else:
                position[0] += 1
                continue
        elif decision(position[0],position[1],0,-1) == 1:
            count2 = 0
            position[2] = 3
            position[1] -= 1
            count += 1
            map_[position[0]][position[1]] = 2
            continue
    if position[2] == 1:
        if decision(position[0],position[1],-1,0) != 1:
            if count2 != 4:
                count2 += 1
                position[2] = 0
                continue
            if decision(position[0],position[1],0,-1) == 0:
                break
            elif decision(position[0],position[1],0,-1) == 1:
                count2 = 0
                position[1] -= 1
                count += 1
                continue
            else:
                position[1] -= 1
                continue
        elif decision(position[0],position[1],-1,0) == 1:
            count2 = 0
            position[2] = 0
            position[0] -= 1
            count += 1
            map_[position[0]][position[1]] = 2
            continue
    if position[2] == 2:
        if decision(position[0],position[1],0,1) != 1:
            if count2 != 4:
                count2 += 1
                position[2] = 1
                continue
            if decision(position[0],position[1],-1,0) == 0:
                break
            elif decision(position[0],position[1],-1,0) == 1:
                count2 = 0
                position[0] -= 1
                count += 1
                continue
            else:
                position[0] -= 1
                continue
        elif decision(position[0],position[1],0,1) == 1:
            count2 = 0
            position[2] = 1
            position[1] += 1
            count += 1
            map_[position[0]][position[1]] = 2
            continue
    if position[2] == 3:
        if decision(position[0],position[1],1,0) != 1:
            if count2 != 4:
                count2 += 1
                position[2] = 2
                continue
            if decision(position[0],position[1],0,1) == 0:
                break
            elif decision(position[0],position[1],0,1) == 1:
                count2 = 0
                position[1] += 1
                count += 1
                continue
            else:
                position[1] += 1
                continue
        elif decision(position[0],position[1],1,0) == 1:
            count2 = 0
            position[2] = 2
            position[0] += 1
            count += 1
            map_[position[0]][position[1]] = 2
            continue
print(count)

# #n,m을 공백으로 구분하여 입력받기
# n, m = map(int,input().split())
# d = [[0] for _ in range(n)]
# #방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
# x,y,direction = map(int, input().split())
# d[x][y] = 1

# #전체 맵 정보를 입력받기
# array = []
# for i in range(n):
#     array.append(list(map(int, input().split())))

# #북,동,남,서 방향 정의
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# #왼쪽으로 회전
# def turn_left():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3
# #시물레이션 시작
# count = 1
# turn_time = 0
# while True:
#     #왼쪽으로 회전
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#     #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
#     if d[nx][ny] == 0 and array[nx][ny] == 0:
#         d[nx][ny] = 1
#         x = nx
#         y = ny
#         count += 1
#         turn_time = 0
#         continue
#     #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
#     else:
#         turn_time += 1
#     #네 방향 모두 갈 수 없는 경우
#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#         #뒤로 갈 수 있다면 이동하기
#         if array[nx][ny] == 0:
#             x = nx
#             y = ny
#         #뒤가 바다로 막혀있는 경우
#         else:
#             break
#         turn_time = 0
#     #정답 출력
#     print(count)