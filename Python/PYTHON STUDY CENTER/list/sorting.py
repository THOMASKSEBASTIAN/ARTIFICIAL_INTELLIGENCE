a=[1,2,3,4,5,6,7,2,3,4]
b=[]
while a:
    min = a[0]
    for i in a:
        if i<=min:
            min=i
    b.append(min)
    a.remove(min)
print(b)

