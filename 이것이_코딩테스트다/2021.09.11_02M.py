import sys
N,M = list(map(int,sys.stdin.readline().split()))
long_list = list(map(int,sys.stdin.readline().split()))


def check(N,dduck):
  result = 0
  for i in N:
    if i >= dduck:
      result += (i - dduck)
    else:
      continue
  return result


def find(N,i):
  result = 0
  h = 0
  t = max(N) - 1
  while h <= t:
    index = (h + t) // 2
    if check(long_list,index) < i:
      t = index - 1
      continue
    elif check(long_list,index) > i:
      result = index
      h = index + 1
      continue
    else:
      result = index
      break
  return result

print(find(long_list,M))