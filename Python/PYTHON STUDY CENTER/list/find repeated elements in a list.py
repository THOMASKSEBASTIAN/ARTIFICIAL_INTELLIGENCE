a=[1,2,3,4,2,3,4,5,6,7,5,11]
e=[]
for i in a:
    if i not in e:
        e.append(i)
    else:
        print(i)