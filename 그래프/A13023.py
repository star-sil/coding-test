#ABCDE
#간선리스트와 인접리스트로 해결한다. 왜냐하면 정점이 서로 연결되어 있는지 확인하면 되기 때문이다.
import sys

N, M = list(map(int,input().split()))
g = [[] for _ in range(N)]
peaples = [[False] * N for _ in range(N)  ]
edges = []

for _ in range(M):
    v1, v2 = list(map(int,input().split()))
    peaples[v1][v2] = peaples[v2][v1] = True
    g[v1].append(v2)
    g[v2].append(v1)
    edges.append((v1,v2))
    edges.append((v2,v1))

M *= 2

for i in range(M):
    for j in range(M):
        A, B = edges[i]
        C, D = edges[j]

        #ABCD가 모두 다른지 확인
        if A == B or A == C or A == D or B == C or B == D or C == D:
            continue
        if not peaples[B][C]:
            continue
        for E in g[D]:
            if A == E or B == E or C == E or D == E:
                continue
            print(1)
            sys.exit(0)
print(0)


