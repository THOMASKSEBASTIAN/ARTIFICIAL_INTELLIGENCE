# method1
a=[4, 5, 6, 7, 8, 9]
length=len(a)
# sum=0
for i in range(length):
    sum=sum+a[i]
print(sum)

# method2
from operator import*
a=[4, 5, 6, 7, 8, 9]
sum=0
for i in a:
    # print(i)
    sum=add(i,0)+sum
print(sum)


# method3
a=[4, 5, 6, 7, 8, 9]
print(sum(a))
