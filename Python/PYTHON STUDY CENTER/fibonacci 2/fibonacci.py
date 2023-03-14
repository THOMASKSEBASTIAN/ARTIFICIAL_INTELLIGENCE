num1=0
num2=1
sum=0
print(num1)
print(num2)
for i in range(1,10):
    sum = num1 + num2
    num1=num2
    num2=sum
    print(sum)

