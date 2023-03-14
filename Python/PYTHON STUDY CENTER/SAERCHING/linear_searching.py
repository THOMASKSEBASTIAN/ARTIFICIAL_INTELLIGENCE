a=[1,3,2,4,5,77]
e=int(input("enter the number"))
flag=0
for i in a:
    if i==e:
        flag=1
        break
    else:
       flag=0
if flag==1:
    print("present")
else:
    print("absent")

