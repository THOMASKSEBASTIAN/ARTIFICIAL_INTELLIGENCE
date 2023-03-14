def add():
    print(num1+num2)
def subtraction():
    print(num1-num2)
def multiplication():
    print(num1*num2)
def division():
    print(num1/num2)
a=int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n.5.stop"))
if a==5:
    print("stop")
elif 1<a>5:
    print("invalid operand")

else:
    num1 = float(input("enter the number"))
    num2 = float(input("enter the number"))

    if a==1:
        add()
    elif a==2:
        subtraction()
    elif a==3:
        multiplication()
    elif a==4:
        division()


