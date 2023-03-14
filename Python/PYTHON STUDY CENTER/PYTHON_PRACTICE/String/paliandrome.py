# method1
String=input("Enter the string")
length=len(String)
string2=""
for i in String[: :-1]:
    string2=string2+i
if String==string2:
    print("paliandrome")


# method 2

String=input("Enter the string")
string2=String[ : : -1]
if String==string2:
    print("Paliandrome")
else:
    print("Not Paliandrome")