
def add_dots(string):
    list=[]
    for i in string:
        list.append(i)
    new=".".join(list)
    return str(new)
# print(add_dots("hello"))
def remove_dots(string):
    string=string.replace(".","")
    return string
# print(remove_dots("h.e.l.l.o"))


print(remove_dots(add_dots("hello")))

