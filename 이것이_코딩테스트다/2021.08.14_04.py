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

# #n,m??? ???????????? ???????????? ????????????
# n, m = map(int,input().split())
# d = [[0] for _ in range(n)]
# #????????? ????????? ???????????? ?????? ?????? ???????????? 0?????? ?????????
# x,y,direction = map(int, input().split())
# d[x][y] = 1

# #?????? ??? ????????? ????????????
# array = []
# for i in range(n):
#     array.append(list(map(int, input().split())))

# #???,???,???,??? ?????? ??????
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# #???????????? ??????
# def turn_left():
#     global direction
#     direction -= 1
#     if direction == -1:
#         direction = 3
# #??????????????? ??????
# count = 1
# turn_time = 0
# while True:
#     #???????????? ??????
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#     #????????? ?????? ????????? ????????? ?????? ?????? ???????????? ?????? ??????
#     if d[nx][ny] == 0 and array[nx][ny] == 0:
#         d[nx][ny] = 1
#         x = nx
#         y = ny
#         count += 1
#         turn_time = 0
#         continue
#     #????????? ?????? ????????? ????????? ?????? ?????? ????????? ????????? ??????
#     else:
#         turn_time += 1
#     #??? ?????? ?????? ??? ??? ?????? ??????
#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#         #?????? ??? ??? ????????? ????????????
#         if array[nx][ny] == 0:
#             x = nx
#             y = ny
#         #?????? ????????? ???????????? ??????
#         else:
#             break
#         turn_time = 0
#     #?????? ??????
#     print(count)