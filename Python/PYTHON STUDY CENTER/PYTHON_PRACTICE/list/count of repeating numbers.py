lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
sum=0

sum2=[i for i in lst if i==10 ]
print(len(sum2))

print(sum2)

# method2
from collections import Counter

# declaring the list
l = [1, 1, 2, 2, 3, 4, 4, 4, 5, 5]

# driver program
x = 3
d = Counter(l)
print('{} has occurred {} times'.format(x), d[x])

# method3

l = [1, 1, 2, 2, 3, 4, 4, 4, 5, 5]
import pandas as pd
count=pd.Series(l).value_counts()
print(count)


