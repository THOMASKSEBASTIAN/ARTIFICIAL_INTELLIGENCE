# method 1

a=[4, 5, 6, 7, 8, 9]
len=len(a)
print(a[-1:-len-1:-1])

# method 2
a=[4, 5, 6, 7, 8, 9]
a.reverse()
print(a)