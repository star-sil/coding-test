# A와 B 2

s = list(input())
t = list(input())


def dfs(a):

    if len(a) == len(s):
        if ''.join(a) == ''.join(s):
            print(1)
            exit()
        return

    if a[-1] == 'A':
        a.pop()
        dfs(a)
        a.append('A')
    if a[0] == 'B':
        a.reverse()
        a.pop()
        dfs(a)
        a.append('B')
        a.reverse()

dfs(t)
print(0)