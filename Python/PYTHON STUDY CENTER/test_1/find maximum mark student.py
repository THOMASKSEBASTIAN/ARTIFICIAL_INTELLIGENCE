student=[("anu",67),("akhil",56),("ravi",88)]

mark=[]
for i in student:
    mark.append(i[1])
maximum=max(mark)
for j in student:
    if maximum==j[1]:
        print(j[0])