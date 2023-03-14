import re
count=0

rules='[abc]'
matcher=re.finditer(rules,"aAvcb @123bnd")
for i in matcher:
    print(i.group())
    print(i.start())
    count=count+1
print(count)