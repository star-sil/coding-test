# N과 M(3)
# set을 사용한 이유는 아무런 조건이 없으면 중복되는 수열이 생길것이라 예상했기 때문이다.
# 하지만 list 자료구조 특성상 먼저 들어온 값 뒤에 값이 쌓이기 때문에 절대 중복되는 수열이 발생할 수 없다.
# 따라서 set 자료구조를 굳이 사용하지 않아도 된다.
# 또한, 오름차순으로 정렬되어 나와야 하는것도 이미 list 자료구조 특성과 로직 때문에 자동으로
# 오름차순으로 정렬되어 출력된다.

n, m = map(int,input().split())

ans = set()
nums = []

def dfs(depth):
    
    if depth == m:
        ans.add(' '.join(map(str,nums)))
        return
    
    for i in range(1,n+1):
        nums.append(i)
        dfs(depth + 1)
        nums.pop()
    
dfs(0)

ans = list(ans)
ans.sort()

for i in ans:
    print(i)