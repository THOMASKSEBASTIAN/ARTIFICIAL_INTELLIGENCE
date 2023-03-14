# a=[4, 5, 1, 2, 9]
# n=int(input("enter the number of elements"))
# a.sort(reverse=True)
# print(a[0:n])

a=[4, 5, 1, 2, 9]
n=int(input("enter the number of elements"))
a.sort()
print(a[-1: -n:-1])