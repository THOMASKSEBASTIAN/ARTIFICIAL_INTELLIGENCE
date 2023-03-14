import re
s=input("enter the string")

# rule='[a-zA-Z\W]{5}'
rule='[^0-9]{5}'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print("valid")
else:
    print("not valid")
