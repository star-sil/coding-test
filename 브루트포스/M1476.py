# 날짜 계산
# 날짜 최대 범위로 나눈 나머지로 준규가 사는 나라의 날짜를 구할때
# 날짜 최대 범위로 나누어 떨어지는 경우 준규가 사는 나라의 날짜는 0이 되는 함정 주의!!
# => 나머지가 0인 경우는 준규가 사는 나라의 최대 날짜 범위 이다.

e, s, m = map(int,input().split())

def changeDate(d,t):
    if d % t == 0:
        return t
    return d % t

ans = 0
while True:
    ans += 1

    if e == changeDate(ans,15) and s == changeDate(ans,28) and m == changeDate(ans,19):
        print(ans)
        break