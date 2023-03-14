def pattern():
    count = 5
    for i in range(5):
        number=i
        for j in range(count):              #for space
            print(end=" ")                  #for space
        count=count-1                       #for space

        for k in range(i):                  #for multiplication
            # print("k",k)
            # print("number",number)
            print(k*number,end=' ')         #for multiplication
        print( )                            #for multiplication
    number=number+1
pattern()                                   #calling function