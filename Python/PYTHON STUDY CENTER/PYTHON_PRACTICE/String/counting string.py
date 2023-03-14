from collections import Counter
test_str = "Gfg is best"
test_str2=test_str.split()
for i in test_str2:

    d=Counter(test_str2)
    print("The count of {0} is {1}".format([i],d[i]))
