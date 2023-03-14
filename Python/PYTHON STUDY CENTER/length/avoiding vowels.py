string=input("enter the string")
v="aeiou"
n=""
for i in string:
    if i not in v:
        n=n+i
print(n)
