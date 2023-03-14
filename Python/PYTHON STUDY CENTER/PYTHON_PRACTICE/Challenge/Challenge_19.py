def all_equal(a):
    for i in a:
        for j in i:
            if i!=j:
                return False
    return  True
print(all_equal(str([1, 3, 1])))