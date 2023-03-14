n=int(input("enter the number of elements"))
for i in range(n):
    if i>1:
        for j in range(2,i):
                if i % j==0:
                    break
        else:
            if i%2!=0:

              print(i)
