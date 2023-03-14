# import re
# s=input("enter the number")
# rule='[a-zA-Z][\w\d]{8}[\d]'
# check=re.fullmatch(rule,s)
# if check is not None:
#     print("valid")
# else:
#     print("not valid")


import re
s=input("enter the number")
rule='[\w\d,_%+-]+[@][g][m][a][i][l][.][c][o][m]'
check=re.fullmatch(rule,s)
if check is not None:
    print("valid")
else:
    print("not valid")