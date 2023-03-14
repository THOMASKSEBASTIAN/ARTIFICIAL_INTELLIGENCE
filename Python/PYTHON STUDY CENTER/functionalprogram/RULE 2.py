import re

# s = input("enter the string")
#
# # rule='[a-zA-Z\W]{5}'
# rule = '[a-z][\W\w]{3,8}[A-Z]'
# matcher = re.fullmatch(rule, s)
# if matcher is not None:
#     print("valid")
# else:
#     print



s = input("enter the string")

# rule='[a-zA-Z\W]{5}'
rule = '[0-9]{4}[a-z\W]'
matcher = re.fullmatch(rule, s)
if matcher is not None:
    print("valid")
else:
    print("not valid")
