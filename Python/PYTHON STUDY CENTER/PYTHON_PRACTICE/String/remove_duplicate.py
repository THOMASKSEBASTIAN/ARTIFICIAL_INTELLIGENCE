string="geeksforgeeks "
string2=""
for i in string:
    if i not in string2:
        string2=string2+i
print(string2)