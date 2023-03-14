import re
s=input("enter the string")

rule='^a[\w\W]*b$'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print("valid")
else:
    print("not valid")
