
def changevalue(func):
    def wrapper(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
        else:
            return func(a, b)
    return wrapper






@changevalue
def sub(n1,n2):
    return n1-n2
print(sub(2,10))