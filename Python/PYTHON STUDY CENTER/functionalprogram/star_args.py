# def printvalue(*args):
#     print(args)
# printvalue



# sum of number input by user
def add(*number):
    sum=0
    for i in number:
        sum=sum+i
    print(sum)
add(3,4,5,3,10)