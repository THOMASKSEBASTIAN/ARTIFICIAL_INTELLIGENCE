# The built-in zip function "zips" two lists. Write your own implementation of this function.
#
# Define a function named zap. The function takes two parameters, a and b. These are lists.
#
# Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b.
#
# You may assume a and b have equal lengths.
#
# If you don't get it, think of a zipper.

def zap(a, b):
    zap_list=[]
    for i in range((len(a))):
        zap_list.append((a[i],b[i]))
    return zap_list
print(zap([0, 1, 2, 3],[5, 6, 7, 8]))