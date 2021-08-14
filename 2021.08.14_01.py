size = int(input())
plan = map(str,input().split())
point = [1,1]
for i in plan:
    if i == 'L':
        if point[1] > 1:
            point[1] -= 1
    if i == 'R':
        if point[1] < size:
            point[1] += 1
    if i == 'U':
        if point[0] > 1:
            point[0] -= 1
    if i == 'D':
        if point[0] < size:
            point[0] += 1
print(point[0],point[1])