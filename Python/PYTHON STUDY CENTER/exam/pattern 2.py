# def patter1():
#     space = 7
#     for i in range(7):
#
#         for k in range(space):
#             print(" ", end="")
#         space = space - 1
#
#         for j in range(i):
#             print("*", end=" ")
#         print(" ")
#
# def patter2():
#     space = 2
#     for i in range(5, 0, -1):
#         for k in range(space):
#             print(" ", end="")
#         space = space + 1
#
#         for j in range(i):
#             print("*", end=" ")
#         print("")
# patter1()
#
# patter2()





space1=4
space2=1
for i in range(4):
    if i>=0 and i<=3:
        for k in range(space1):
            print(end=" ")
        space1-=1
        for j in range (i):
            print("*",end=" ")
        print("")

for i in range(3,0,-1):
    if i>=0 and i<=3:
        for k in range(space2):
            print(end=" ")
        space2+=1
        for j in range (i):
            print("*",end=" ")
        print("")


