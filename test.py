li = [1,2,3,0,1,2]
for i in li:
    try:
        print(1 / i)
    except e:
        print(e)
    finally:
        print('se')