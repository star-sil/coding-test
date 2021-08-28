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