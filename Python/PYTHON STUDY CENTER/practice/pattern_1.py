# pyramid shape
def pattern1():
    line = 5
    for i in range(5):
        for k in range(line):
            print(end=" ")

        for j in range(i):
            print("*",end=" ")
        print()
        line=line-1
# pattern()


# parellelogram
# def pattern():
#     for i in range(5):
#         for k in range(i):
#             print(end=" ")
#
#         for j in range(5):
#             print("*",end=" ")
#         print()
#
# pattern()


# inveretd pyramid shape
def pattern():
    line = 0
    for i in range(5,0,-1):
        for k in range(line):
            print(end=" ")

        for j in range(i):
            print("*",end=" ")
        print()
        line=line+1
pattern1()
pattern()