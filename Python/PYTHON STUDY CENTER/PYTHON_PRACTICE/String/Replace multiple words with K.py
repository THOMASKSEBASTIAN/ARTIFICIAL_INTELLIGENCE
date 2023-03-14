# Python3 code to demonstrate working of
# Replace multiple words with K
# Using join() + split() + list comprehension

# initializing string
test_str = 'Geeksforgeeks is best for geeks and CS'
print(type(test_str))

# printing original string
print("The original string is : " + str(test_str))

# initializing word list
word_list = ["best", 'CS', 'for']

# initializing replace word
repl_wrd = 'gfg'
test_str2=[]
# Replace multiple words with K
# Using join() + split() + list comprehension
# res = ' '.join([repl_wrd if idx in word_list else idx for idx in test_str.split()])

for i in test_str.split():
    if i in word_list:
        i=repl_wrd
        test_str2.append(i)
    else:
        test_str2.append(i)
print(test_str2)
