import sys
N = eval(input())
N_list = list(map(int,sys.stdin.readline().rstrip().split()))
M = eval(input())
M_list = list(map(int,sys.stdin.readline().rstrip().split()))
N_list = sorted(N_list)

def find(N,i):
  h = 0
  t = len(N) - 1
  while h <= t:
    index = (h + t) // 2
    if N[index] > i:
      t = index - 1
      continue
    elif N[index] < i:
      h = index + 1
      continue
    else:
      return 'yes'
  return 'no'

for i in M_list:
  print(find(N_list,i),end=" ")