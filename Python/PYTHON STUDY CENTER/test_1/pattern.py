initial=int(input("enter the initial range"))
final=int(input("enter the final range"))
for i in range(initial,final):
    if i%2==0:
        for a in range (5,0,-1):
            for b in range(a):
                print(i,end=" ")
            print()
    else:
        for a in range(1,5):
            for b in range(a):
                print(i, end=" ")
            print()