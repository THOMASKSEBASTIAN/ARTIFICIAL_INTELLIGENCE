n1=int(input("enter the n1"))
n2=int(input("enter the n2"))
try:
    print(n1/n2)
except:
    print("zero division error")
finally:
    print("hai")