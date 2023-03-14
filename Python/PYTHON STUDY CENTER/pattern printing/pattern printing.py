space=4
for i in range(4):
    for k in range(space):
        print(end=" ")
    space=space-1
    for j in range(i):
        print("*",end=" ")
    print(" ")