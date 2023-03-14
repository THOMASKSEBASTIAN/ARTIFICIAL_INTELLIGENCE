#vowels remove from a list
# element=input("enter the element")
# a="aeiou"
# new=""
# for i in element:
#     if i not in a:
#         new=new+i
# print(new)


# pattern
# space=10
# for i in range(5):
#
#     for k in range(space):
#         print(end=" ")
#     space=space-2
#     for j in range(i):
#         print("*",end=" ")
#     print(" ")



# pattern 2

space=5
for i in range(5):

    for k in range(space):
        print(end=" ")
    space=space-1
    for j in range(i):
        print("*",end=" ")
    print(" ")
for i in range(5,0,-1):
    for k in range(space):`
        print(end=" ")
    space=space+1
    for j in range(i):
        print("*",end=" ")

    print(" ")