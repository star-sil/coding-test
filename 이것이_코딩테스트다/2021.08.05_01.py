from sys import stdin
n = int(stdin.readline())
possible_time = []
confer_times = []
for i in range(n):
    confer_times.append(list(map(int, stdin.readline().split())))
confer_times.sort(key=lambda x: (x[1], x[0]))
for i in confer_times:
    if len(possible_time) == 0:
        possible_time.append(i)
    elif possible_time[-1][1] <= i[0]:
        possible_time.append(i)
print(len(possible_time))
