a=[1,5,8,99,34,21,56,76,98,11,24,65,78]
prime=[]
nonprime=[]
for i in a:

    for j in range(2,i):
        if i%j==0:
            nonprime.append(i)
            break

        else:
            prime.append(i)


print(prime)
print(nonprime)