# Challenge
# Up and down
# Define a function named up_down that takes a single number as its parameter. Your function return a tuple containing two numbers; the first should be one lower than the parameter, and the second should be one higher.
#
# For example, calling up_down(5) should return (4, 6).

# Tuple is immutable

def up_down(a):
    return((a-1,a+1))
print(up_down(9))
