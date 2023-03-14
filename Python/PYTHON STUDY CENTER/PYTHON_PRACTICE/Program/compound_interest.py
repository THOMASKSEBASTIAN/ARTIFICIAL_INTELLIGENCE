# Finding the simple interest
def interest(p,t,r):
    print("The principal amount is ",p)
    print("The number of years  is ", t)
    print("The rate of %  is ", r)
    amount=p*(1+r/100)**t
    print("The amount is ",amount)
    print("The compound interest is  ", amount-p)

p= int(input("Enter the principal value"))
t=int(input("Enter the number of years you want to deposit"))
r=int(input("Enter the rate of interest"))
interest(p,t,r)