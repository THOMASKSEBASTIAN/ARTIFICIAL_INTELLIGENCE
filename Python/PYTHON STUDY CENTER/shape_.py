s=10
for i in range(10):
    for k in range(s):
        print(end=" ")

    for j in range(i):
        print("*",end=" ")
    s=s-1
    print('')
