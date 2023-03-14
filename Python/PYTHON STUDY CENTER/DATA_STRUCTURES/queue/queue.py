def enqueue():
    if len(l) < size:
        new = int(input("enter the element"))
        l.append(new)
    else:
        print("limit exceed")
    print(l)

def dequeue():
    if len(l) > 0 and len(l) <=size:
        l.remove(l[0])

    elif len(l) <= 0:
        print("cant remove")
    print(l)


size=int(input("enter the size"))

l=[]
while True:
    o = int(input("enter the option \n1.enqueue\n2.dequeue"))
    if o==1:
        enqueue()
    elif o==2:
        dequeue()



