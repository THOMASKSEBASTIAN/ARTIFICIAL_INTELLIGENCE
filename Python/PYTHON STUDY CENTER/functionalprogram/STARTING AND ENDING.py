import re
s=input("enter the string")

# rule='[a-zA-Z\W]{5}'
rule='^\d[a-zA-Z0-9\W]{3}*\d$'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print("valid")
else:
    print("not valid")
