a=[2,3,4,33,55,66,77]
prime=[]
nonprime=[]
for i in a:
    if i>1:
        for j in range(2,i):
            if i%j==0:
                nonprime.append(i)
                break
        else:
            prime.append(i)
print(nonprime)
print(prime)