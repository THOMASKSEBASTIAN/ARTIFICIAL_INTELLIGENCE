def all_equal(list):
    a=list[1]
    for i in list:
        if a!=i:
            break
    else:
        return(True)
print(all_equal([1, 1, 1]))