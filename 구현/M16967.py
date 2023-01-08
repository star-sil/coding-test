# 배열 복원하기
# 리스트 출력할때 앞에 * 붙이면 [ ] 생략해서 출력 가능하다.

h, w, x, y = map(int,input().split())

g = [list(map(int,input().split())) for _ in range(h+x)]

for i in range(h):
    for j in range(w):
        if i + x < h and j + y < w:
            g[i+x][j+y] -= g[i][j]

for i in range(h):
    print(*g[i][:w])