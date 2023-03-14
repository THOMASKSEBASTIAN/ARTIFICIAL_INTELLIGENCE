test_str = "GeeksForGeeks"
test_str2=" "
len=len(test_str)
for i in range (len):
    if i!=2:
        test_str2=test_str2+test_str[i]
print(test_str2)