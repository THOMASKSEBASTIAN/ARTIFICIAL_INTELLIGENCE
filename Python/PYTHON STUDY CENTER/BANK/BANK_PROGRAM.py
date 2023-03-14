Fixed_amount=1000
a=int(input("enter the withdrawal amount"))
if a>Fixed_amount:
    print("insufficient balance")
else:
    print(Fixed_amount-a)