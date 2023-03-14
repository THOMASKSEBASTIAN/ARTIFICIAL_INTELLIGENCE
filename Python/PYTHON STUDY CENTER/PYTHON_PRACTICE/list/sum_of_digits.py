test_list = [12, 67, 98, 34]
test_list2=[]
sum=0
for i in test_list:
    i=str(i)
    for j in i:
        j=int(j)
        sum=sum+j
    # print(sum)
    test_list2.append((sum))
    sum=0
print(test_list2)
