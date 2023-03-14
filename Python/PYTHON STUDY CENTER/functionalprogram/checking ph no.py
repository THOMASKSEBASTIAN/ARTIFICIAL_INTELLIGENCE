import re
s=input("enter the number")
rule='\d{10}'
matcher=re.fullmatch(rule,s)
if matcher is not  None:
    print("valid")
else:
    print("Invalid")

