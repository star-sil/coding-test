dic = {'a' : 1,'b' : 2,'c' :3,'d' : 4,'e' : 5,'f' : 6,'g' : 7,'h': 8}
input = input()
point = [int(input[1]),dic[input[0]]]
count = 0
if point[0] <= 6 and point[1] <= 7:
    count += 1
if point[0] >= 3 and point[1] <= 7:
    count += 1
if point[0] <= 6 and point[1] >= 2:
    count += 1
if point[0] >= 3 and point[1] >= 2:
    count += 1

if point[1] <= 6 and point[0] <= 7:
    count += 1
if point[1] >= 3 and point[0] <= 7:
    count += 1
if point[1] <= 6 and point[0] >= 2:
    count += 1
if point[1] >= 3 and point[0] >= 2:
    count += 1

print(count)

# #다른 풀이
# # ord() 해당 문자의 아스키코드값 반환
# input = input()
# row = int(input[1])
# column = int(ord(input[0])) - int(ord('a')) + 1

# steps = [(-2,-1),(-1,-2),(1,-2),(-1,+2),(2,-1),(2,1),(1,2),(-2,1)]

# result = 0
# for step in steps:
#     next_row = row + step[0]
#     next_column = column + step[1]

#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <=8:
#         result += 1
# print(result)