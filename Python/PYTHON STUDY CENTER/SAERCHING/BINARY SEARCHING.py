a=[1,2,3,4,5,6,7,87,10,9,2]
e=int(input("enter the number"))
a.sort()
flag=0
low=0
upper=len(a)-1
while low<=upper:
    mid=(low+upper)//2
    if a[mid]==e:
        flag=1
        break
    elif e>a[mid]:
        low=mid+1
    elif e<a[mid]:
        upper=mid-1
if flag==1:
    print("present")
else:
    print("absent")