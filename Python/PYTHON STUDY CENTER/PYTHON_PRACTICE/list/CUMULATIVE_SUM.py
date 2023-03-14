# method1
list = [10, 20, 30, 40, 50]
output=[]
num1=0
for i in list:
    num2=i
    sum=num1+num2
    output.append(sum)
    num1=sum

print(output)


# method2
list = [10, 20, 30, 40, 50]
list2=[]
sum=0
for i in list:
    sum=sum+i
    list2.append(sum)
print(list2)




