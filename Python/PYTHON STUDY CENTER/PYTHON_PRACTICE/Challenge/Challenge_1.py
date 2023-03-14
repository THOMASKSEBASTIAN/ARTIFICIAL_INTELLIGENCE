# Challenge
# Capital indexes
# Write a function named capital_indexes. The function takes a single parameter, which is a string.
# Your function should return a list of all the indexes in the string that have capital letters.
#
# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

list = []
string_s1 = "HeLlO"


def capital_indexes(string):
    for i in enumerate(string):
        if i[1].isupper():
            list.append(i[0])

    return list


print(capital_indexes(string_s1))
