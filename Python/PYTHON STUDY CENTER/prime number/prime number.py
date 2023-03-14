def prime():
    initial=int(input("enter the initial value"))
    final = int(input("enter the initial value"))
    for i in range(initial,final):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)
prime()
