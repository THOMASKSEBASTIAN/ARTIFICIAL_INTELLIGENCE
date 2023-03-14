def odd(num1,num2):
    sum=0
    for i in range(num1,num2):
        if i%2!=0:
            sum=sum+i
    print(sum)
odd(1,10)
            