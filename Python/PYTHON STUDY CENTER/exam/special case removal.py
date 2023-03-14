d=open("text.txt","r")
new=" "
symbol="!@#$%^&*()_+{}:|<>?[];\,./"
for i in d:
    f=i.rstrip("\n")
    # print(f)
    for j in f:
        # print(j)
        if j not in symbol:
            new=new+j
    #
    print(new)