# Python program to print
# ASCII Value of Character

# In c we can assign different
# characters of which we want ASCII value
#
# c = 'g'
# # print the ASCII value of assigned character in c
# print("The ASCII value of '" + c + "' is", ord(c))


# String=input("Enter a string:")

text = input("Enter a String: ")
textlength=len(text)
print(textlength)
for char in text:
    print(char,":",ord(char))