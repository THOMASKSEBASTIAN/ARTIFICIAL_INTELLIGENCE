prime=[]
def prim():
    initial=int(input("enter the number"))
    final = int(input("enter the number"))
    for i in range(initial,final):
        if i >1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                prime.append(i)
        # else:
        #     print("It is not a prime number")
    print("The prime numbers are", prime)


prim()