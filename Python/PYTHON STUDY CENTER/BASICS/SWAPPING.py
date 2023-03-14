# method1
num1=2
num2=3
num1,num2=num2,num1
print(num1,num2)

# method2

num1=2
num2=3
temp=num1
num1=num2
num2=temp
print(num1,num2)


# method3

num1=2
num2=3
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(num1,num2)

