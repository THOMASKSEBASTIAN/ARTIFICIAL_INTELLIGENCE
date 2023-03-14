# Finding the simple interest
def interest(p,n,r):
    print("The principal amount is ",p)
    print("The number of years  is ", n)
    print("The rate of %  is ", r)
    simple_interest=(p*n*r)/100
    print("The simple interest is ",simple_interest)
p=int(input("Enter the principal value"))
n=int(input("Enter the number of years you want to deposit"))
r=int(input("Enter the rate of interest"))
interest(p,n,r)