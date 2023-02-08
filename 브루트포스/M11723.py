# 집합
from sys import stdin

def add(s, x):
    return s | (1 << x)

def remove(s, x):
    return s & ~(1 << x)

def check(s, x):
    if s & (1 << x):
        return 1
    else:
        return 0

def toggle(s, x):
    return s ^ (1 << x)

def empty():
    return 0

m = int(input())

s = 0
for _ in range(m):
    commandList = list(stdin.readline().split())
    if len(commandList) > 1:
        x = int(commandList[1])
    command = commandList[0]

    if command == 'add':
        s = add(s, x)
    elif command == 'remove':
        s = remove(s, x)
    elif command == 'check':
         print(check(s, x))
    elif command == 'toggle':
        s = toggle(s, x)
    elif command == 'all':
        s = 2097150
    else:
        s = empty()