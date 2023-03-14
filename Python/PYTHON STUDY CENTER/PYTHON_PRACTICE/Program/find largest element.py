a=[2,4,5,34,4,2]
length=len(a)
min=a[0]
for i in range(length):
    if a[i]<min:
        a.remove(min)
        min=a[i]
else:
    print(min)


