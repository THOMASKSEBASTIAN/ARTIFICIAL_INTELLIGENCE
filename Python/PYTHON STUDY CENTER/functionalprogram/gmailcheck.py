import re
s=input("enter the mail id")

rule='[\w._%+-]+[@][g][m][a][i][l][.][c][o][m]'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print("valid")
else:
    print("not valid")