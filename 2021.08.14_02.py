input = int(input())
time = input * 3600 + 3599
count = 0
while(time > 0):
    c = str(time // 360)
    m = str((time - int(c) * 360) // 60)
    s = str(time - int(c) * 360 - int(m) * 60)
    if ('3' in c) or ('3' in m) or ('3' in s):
        count += 1
    time -= 1
print(count)

##다른 풀이   
# h = int(input())

# count = 0
# for i in range(h + 1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1