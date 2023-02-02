# 암호 만들기
# 해당 로식으로 문제를 풀수 있지만 더 정확한 로직이 있다.

b = {'a','e','i','o','u'}
l, c = map(int,input().split())
a = list(input().split())
a.sort()
password = []


# 구성 개수, 자음개수, 모음 개수, 시작 인덱스
def make_password(cnt, consonant, collection, s):

    if consonant >= 1 and collection >= 2 and cnt == l:
        print(''.join(map(str,password)))

    for i in range(s, len(a)):
        password.append(a[i])
        if a[i] in b:
            make_password(cnt+1,consonant+1,collection,i+1)
        else:
            make_password(cnt+1,consonant,collection+1,i+1)
        password.pop()

make_password(0,0,0,0)