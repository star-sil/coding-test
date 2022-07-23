#강의실 배정
import heapq
N = int(input())

time = []
for _ in range(N):
    data = list(map(int, input().split()))
    time.append(data)

time.sort()
lecture = []
heapq.heappush(lecture,time[0][1])

for i in range(1,N):
    if lecture[0] > time[i][0]:
        heapq.heappush(lecture,time[i][1])
    else:
        heapq.heappop(lecture)
        heapq.heappush(lecture,time[i][1])
    
print(len(lecture))