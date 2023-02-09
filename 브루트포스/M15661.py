# 링크와 스타트 - 20m 15s

n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]
result = float('inf')
def dfs(s, a, b):

    # 팀인원이 조건에 맞을때
    if len(a) + len(b) == n:
        if len(a) > 0 and len(b) > 0:
            # a팀 능력치 구하기
            aAbility = 0
            for i in a:
                for j in a:
                    if i != j:
                        aAbility += ability[i][j]

            bAbility = 0
            for i in b:
                for j in b:
                    if i != j:
                        bAbility += ability[i][j]

            return abs(aAbility-bAbility)
        else:
            return float('inf')

    global result
    for i in range(s, n):
        link = dfs(i+1,a+[i],b)
        start = dfs(i+1,a,b+[i])

        result = min(result,min(link,start))

    return result

print(dfs(0,[],[]))