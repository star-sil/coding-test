# 부분합
n, s = map(int,input().split())
sequence = list(map(int,input().split()))
i, j = 0, 0
add = 0
ans = float('inf')


while True:

    if add < s:

        if j == n:
            break

        add += sequence[j]
        j += 1

    elif add >= s:
        ans = min(ans, j - i)
        add -= sequence[i]
        i += 1


print(0 if ans == float('inf') else ans)