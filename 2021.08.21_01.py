
a = int(input())
b = int(input())
input_list = list()
friend = list()
friend_ = [i for i in range(2,a+1)]
for i in range(b):
  n,m = list(map(int,input().split()))
  if n <= m:
    input_list.append([n,m])
    continue
  input_list.append([m,n])

for i in input_list:
  if 1 in i:
    friend.append(i[1])
    friend_.remove(i[1])
    continue

for i in input_list:
  if i[0] in friend or i[1] in friend:
    if i[1] in friend_:
      friend_.remove(i[1])
    if i[0] in friend_:
      friend_.remove(i[0])
  
print(a - len(friend_) -1)