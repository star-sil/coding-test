import re
li = []
def plus(l):
    i = l.split('+')
    result = 0
    for j in i:
        j = j.lstrip('0')
        if len(j) == 0:
            j = 0
        result += int(j)
    return str(result)
input = input()
input = input.split('-')
for i in input:
    li.append(plus(i))
result = '-'.join(li)
print(eval(result))