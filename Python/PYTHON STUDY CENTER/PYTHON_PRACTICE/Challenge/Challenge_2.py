# Challenge
# Middle letter
# Write a function named mid that takes a string as its parameter. Your function should extract
# and return the middle letter. If there is no middle letter, your function should return the empty string.
#
# For example, mid("abc") should return "b" and mid("aaaa") should return "".
def mid(string):
    string_2=""
    mid_value_1=len(string)%2
    if mid_value_1 == 0:
        return (string_2)

    else:
        mid_value = int((len(string)-1) / 2)
        letter=string[mid_value]
        return (letter)
print(mid("abc"))