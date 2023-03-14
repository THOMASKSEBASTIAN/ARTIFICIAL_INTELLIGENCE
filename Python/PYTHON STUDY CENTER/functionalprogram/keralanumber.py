import re
s=input("enter the number")
rule='[K][L][0-9]{2}[A-Z]{1,2}[0-9]{4}'

matcher=re.fullmatch(rule,s)
if matcher is not  None:
    print("valid")
else:
    print("Invalid")