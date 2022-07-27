#바이러스 116ms
from collections import deque
input_list = dict()
com = eval(input())
relative = eval(input())

def make_relation(re):
    if re[0] in input_list:
        input_list[re[0]].add(re[1])
    else:
        input_list[re[0]] = {re[1]}
    if re[1] in input_list:
        input_list[re[1]].add(re[0])
    else:
        input_list[re[1]] = {re[0]}

for i in range(relative):
    tmp = list(map(int,input().split()))
    make_relation(tmp)

#너비우선 탐색
que = deque()
check = [0]*com
if 1 in input_list.keys():
    check[0] = 1
    for i in input_list[1]:
        que.append(i)
        check[i-1] = 1

while len(que) > 0:
    computer = que.popleft()
    if computer in input_list.keys():
        for i in input_list[computer]:
            if check[i-1] == 0:
                check[i-1] = 1
                que.append(i)

print(check.count(1)-1)