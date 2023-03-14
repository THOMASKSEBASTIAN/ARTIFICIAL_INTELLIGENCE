# quantifiers
# x='a+' a including group
# x='a*'count including zero number of a
# x='a?' count a as each including zero no of a
# x='a{2}' 2 no of a position
# x='a{2,3}'minimum 2 a and maximum 3 a
# x='^a' check starting with async
# x='a$'check ending with a


import re
count=0

rules='a+'
matcher=re.finditer(rules,"abca")
for i in matcher:
    print(i.group())
    print(i.start())
    count=count+1
print(count)