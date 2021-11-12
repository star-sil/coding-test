class hello:
    def __init__(self,count):
        self.count = count
        pass
    def fprint(self):
        print(self.count)
li = []
for i in range(1,4):
    a = hello(i)
    li.append(a)
print(li)

for i in li:
    i.fprint()