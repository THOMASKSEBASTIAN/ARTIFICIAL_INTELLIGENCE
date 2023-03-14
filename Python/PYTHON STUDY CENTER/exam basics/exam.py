# lst = [1, 0, 7, 5, 9, 2, 3, 5, 7, 2, 0, 1, 10]
# new=[]
# # for i  in lst:
# #     if i not in new:
# #      new.append(i)
# #
# # print(new)
#
#
# Students =[('anu',67),('amal',69),('arun',65)]
# new=[]
# for i in Students:
#     print(i)
#
# for i in range(6):
#     for j in range(i):
#         print(1,end=" ")
#     print(" ")
# for j in range(5,0,-1):
#     for j in range(j):
#         print(2,end=" ")
#     print(" ")
# for k in range(1,6):
#     for j in range(k):
#         print(3,end=" ")
#     print(" ")
# for j in range(5,0,-1):
#     for j in range(j):
#         print(4,end=" ")
#     print(" ")


# b = [3, 77, 0, 5, 33, 6, 22, 5, 90, 32, 56, 78, 98, 54, 67, 11, 34, 88]
# c=int(len(b)/2)-1
# b.remove(b[c])
# print(b)

# number=input("enter the number")
#
# C=number[: :-1]
# print(C)


# new=[i for i in range(1,100) if i%5==0]
#/
# print(new)


a=[1,2,3]
a.append(3)
b=[2,3,4]
b.extend(a)
print(a)
print(b)