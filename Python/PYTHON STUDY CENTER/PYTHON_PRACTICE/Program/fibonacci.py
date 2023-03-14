def fibonacci():
    number=int(input("enter the number"))
    n1=0
    n2=1
    sum=0
    print(n1)
    print(n2)
    for i in range(number):
        if n2<number:
            sum=n1+n2
            print(sum)
            n1=n2
            n2=sum
        else:
            break
fibonacci()