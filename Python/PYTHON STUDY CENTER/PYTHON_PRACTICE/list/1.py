# method1

list comprehension
list1 = [11, 5, 17, 18, 23, 50]

# will create a new list,
# excluding all even numbers
list1 = [elem for elem in list1 if elem % 2 != 0]

print(list1)



# method2

list1 = [11, 5, 17, 18, 23, 50]
del list1[1:5]
print(list1)