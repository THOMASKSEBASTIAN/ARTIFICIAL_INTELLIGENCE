from collections import Counter
s="GeeksforGeeks"
d=Counter(s)
# print(d)
k = max(d,key=d.get)
print(k)
