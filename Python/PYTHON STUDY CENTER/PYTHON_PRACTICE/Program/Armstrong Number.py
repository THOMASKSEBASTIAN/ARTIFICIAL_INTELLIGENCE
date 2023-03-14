# number=(input("enter the number"))
# length=(len(number))
# sum=0
# for i in range(len(number)):
#     print(number[i])
#     sum2=int(number[i])**length
#     sum=sum+sum2
# sum=str(sum)
# if sum==number:
#     print("This is an armstrong")
# else:
#     print("This is not an armstrong")



number=input("Enter the number")
length=len(number)
sum=0
for i in number:
    number2=int(i)**length

    sum=sum+number2
if sum==int(number):
    print("armstrong")
else:
    print("not armstrong")



