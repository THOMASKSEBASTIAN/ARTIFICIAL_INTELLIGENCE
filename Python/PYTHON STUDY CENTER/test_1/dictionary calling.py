d={}
f=open("text.txt","r")
for i in f:
    c=i.upper()
    s=c.rstrip("\n").split(" ")
    # print(s)
    for j in s:
        if j not in d:
            d.update({j:1})
        else:
            value=d[j]
            value += 1
            d.update({j:value})

print(d)