# stack, que, linked list, graph

# stack
def insert():
    if len(list) < size:
        add = int(input("enter the element"))
        list.append(add)
    else:
        print("limit reached")
    print(list)

def remove():
    if len(list)>0 and len(list)<=size :
        list.pop()
    elif len(list)<=0:
        print("empty list")
    print(list)

size=int(input("enter the size"))
list=[]
while True:
    o=int(input("enter the option\n 1. push\n2.pop"))
    if o==1:
        insert()
    elif o==2:
        remove()





