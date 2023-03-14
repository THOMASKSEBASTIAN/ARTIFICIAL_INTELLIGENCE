def prime(num1,num2):
    sum=0
    for i in range(num1,num2):
        if i>1:
            for j in range (2,i):
                if i%j==0:
                    break
            else:
                sum=sum+i
    print(sum)
prime(1,5)