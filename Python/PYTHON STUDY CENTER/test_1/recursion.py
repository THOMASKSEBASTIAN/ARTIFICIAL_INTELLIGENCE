
def fact(num):
    if num==0 or num==1:
        return 1
    elif num>1:
        factorial=num*fact(num-1)
        num=num-1
        return factorial
print (fact(5))