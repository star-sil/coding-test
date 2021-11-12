#나무 자르기
import sys
N, M = map(int,sys.stdin.readline().split())
Trees = [int(i) for i in sys.stdin.readline().split()]
Height = [i for i in range(0,max(Trees))]
results = [[0] for _ in range(len(Height))]

for i in Height: #이구간에서 이미 시간복잡도가 너무 높아 초과되었다.
    result = 0
    for j in Trees:
        if(j > i):
            result += (j - i)
    results[i] = result

while(1):
    if(M in results):
        print(results.index(M))
        break
    else:
        M += 1