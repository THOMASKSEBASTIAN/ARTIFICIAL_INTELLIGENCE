element=input("enter the string")
vowel="aeiou"

for i in element:
    if i not in vowel:
        print(i,end="")