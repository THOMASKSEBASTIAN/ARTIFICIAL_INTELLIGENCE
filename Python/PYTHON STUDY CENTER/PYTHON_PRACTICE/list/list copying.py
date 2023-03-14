# 1. Using the slicing technique
# This is the easiest and fastest way to clone a list. This method is considered when we want to modify a list and
# also keep a copy of the original. In this, we make a copy of the list itself, along with the reference. This process
# is also called cloning. This technique takes about 0.039 seconds and is the fastest technique.

def Cloning(li1):
    li_copy = li1[:]
    return li_copy


# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)
#
#
#
# # method2
li3=[]
li3.extend(li1)
print(li3)


