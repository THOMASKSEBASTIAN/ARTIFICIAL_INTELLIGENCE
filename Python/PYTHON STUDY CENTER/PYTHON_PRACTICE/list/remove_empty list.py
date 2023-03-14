# Python3 code to Demonstrate Remove empty List
# from List using list comprehension

# Initializing list
test_list = [5, 6, [], 3, [],[], 9]
ele=[i for i in test_list if i!=[]]
print(ele)

# method2
# Python Code to Remove empty List from List

def empty_list_remove(input_list):
    new_list = []
    for ele in input_list:
        if ele:
            new_list.append(ele)
    return new_list


# input list values
input_list = [5, 6, [], 3, [], [], 9]

# print initial list values
print(f"The original list is : {input_list}")
# function-call & print values
print(f"List after empty list removal : {empty_list_remove(input_list)}")