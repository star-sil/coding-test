# 경사로

def go(a, l):
    n = len(a)
    c = [False] * n
    for i in range(1, n):
        # 이전 칸과 크기가 다를 경우
        if a[i-1] != a[i]:
            # 두 칸의 높이 차이를 구한다.
            diff = abs(a[i]-a[i-1])
            # 높이 차이가 1이어야 한다.
            if diff != 1:
                return False
            # 오른쪽 칸이 더 클경우
            if a[i-1] < a[i]:
                for j in range(1, l+1):
                    # 경사로 범위보다 작은경우
                    if i-j < 0:
                        return False
                    # 경사로 놓을 블록이 처음 경사로 놓는 블록과 같은 높이가 아닌 경우
                    if a[i-1] != a[i-j]:
                        return False
                    # 경사로 놓는 곳에 또 놓는 경우
                    if c[i-j]:
                        return False
                    # 경사로를 놓는다.
                    c[i-j] = True
            else: # 왼쪽 칸이 더 크거나 같은경우 앞서 체크한 것과 같은 방식으로 체크
                for j in range(l):
                    if i+j >= n:
                        return False
                    if a[i] != a[i+j]:
                        return False
                    if c[i+j]:
                        return False
                    c[i+j] = True
    return True

# 지도 크기, 경사로 길이
n,l = map(int,input().split())
# 지도
a = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    # 지도에서 행
    d = a[i]

    # 지도에서 갈 수 있는지 확인
    if go(d, l):
        ans += 1

for j in range(n):
    # 지도에서 열
    d = [a[i][j] for i in range(n)]
    if go(d,l):
        ans += 1
print(ans)

