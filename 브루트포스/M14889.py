# 스타트와 링크
# 종료 조건 잘 파악하기!!
# 시간 복잡도 4억이 넘는데 강의 보면서 계산해보기

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

startTeam = []
linkTeam = []


def make_team(index, startTeam, linkTeam):

    if index == n:
        if len(startTeam) == n // 2 and len(linkTeam) == n // 2:
            startScore = 0
            for i in startTeam:
                for j in startTeam:
                    startScore += a[i][j]

            linkScore = 0
            for i in linkTeam:
                for j in linkTeam:
                    linkScore += a[i][j]

            return abs(startScore - linkScore)
        else:
            return float('inf')

    startTeam.append(index)
    t1 = make_team(index+1, startTeam, linkTeam)
    startTeam.pop()
    linkTeam.append(index)
    t2 = make_team(index+1, startTeam, linkTeam)
    linkTeam.pop()

    return min(t1, t2)


print(make_team(0,startTeam,linkTeam))



