s = "This is a python language"
s=s.split()
for i in s:
    length=len(i)
    if length%2==0:
        print(i)