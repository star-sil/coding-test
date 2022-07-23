#공주님의 정원
#이 문제는 꽃 피고지는 시기 리스트(dates)를 반복하면서 제거하면 안되고 탐색한 다음 index부터 시작해야한다.
#특히 탐색했던 index 부터 리스트를 읽기 시작하면 시간초과가 되므로 조심해야한다.
#탐색 했던 index 부터 읽기 시작하면 무한 루프에 빠질수 있다.
#시작과 끝이 같은 날짜 뒤에 바로 이어서 필 꽃이 없는 경우에 무한 루프에 빠진다. 0이 출력되야함
# 3
# 1 13 9 31
# 9 31 9 31
# 10 1 10 2
input = __import__('sys').stdin.readline

def dateToValue(month, day):
    return month * 100 + day

N = int(input())

prince = [3,1,11,30]
dates = []

maxDate = 301;
for _ in range(N):
    data = list(map(int,input().split()))
    dates.append([dateToValue(data[0],data[1]),dateToValue(data[2],data[3])])
dates.sort()

index = 0
count = 0

while index < N:
   
    maxEndDate = 0
    if maxDate > 1130:
        break

    count += 1
    for i in range(index,N):
        if maxDate >= dates[i][0]:
            maxEndDate = max(maxEndDate,dates[i][1])
            index = i
        else:
            break
    index += 1
    maxDate = maxEndDate

print(0 if maxDate <= 1130 else count)