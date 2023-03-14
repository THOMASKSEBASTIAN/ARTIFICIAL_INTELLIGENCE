import re
s=open('registration number.txt','r')
d=open('python.txt','w')
for i in s:
    f=i.rstrip("\n")
    # print(f)
    rule = '[P][Y][0-9]{2}'
    matcher = re.fullmatch(rule, f)
    if matcher is not None:
        d.write(f)
        d.write("\n")

