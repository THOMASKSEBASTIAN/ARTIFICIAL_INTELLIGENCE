arr = {10, 20, 80, 30, 60, 50,110, 100, 130, 170}
# print(type(arr))
arr=list(arr)
# print(arr)
# print(type(arr))
x=int(input("Enter the number\n"))
for i in arr:
    if i==x:
        print(arr.index(i))

